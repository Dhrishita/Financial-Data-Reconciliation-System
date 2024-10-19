import mysql.connector
import pandas as pd
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

# Database credentials
username = 'root'
password = 'Dhrishita@051805'
host = 'localhost'  # Use your MySQL server IP if it's remote

# Connecting to company_ledger_db
company_ledger_connection = mysql.connector.connect(
    host=host,
    user=username,
    password=password,
    database='company_ledger_db'
)

# Connecting to bank_transactions_db
bank_transactions_connection = mysql.connector.connect(
    host=host,
    user=username,
    password=password,
    database='bank_transactions_db'
)

# Function to fetch data from both database and table
def fetch_data(connection, table_name):
    query = f"SELECT * FROM {table_name};"
    return pd.read_sql(query, connection)

# Fetch data
company_ledger_df = fetch_data(company_ledger_connection, 'company_ledger')
bank_transactions_df = fetch_data(bank_transactions_connection, 'bank_transactions')

# Close the connections
company_ledger_connection.close()
bank_transactions_connection.close()

# Displaying the dataframes
print("Company Ledger Data:")
print(company_ledger_df.head())

print("\nBank Transactions Data:")
print(bank_transactions_df.head())

# Reconciliation Logic
# Step 1: Find missing in bank (those present in company ledger but not in bank transactions)
missing_in_bank = company_ledger_df[~company_ledger_df['transaction_id'].isin(bank_transactions_df['transaction_id'])]

# Step 2: Find missing in ledger (those present in bank transactions but not in company ledger)
missing_in_ledger = bank_transactions_df[~bank_transactions_df['transaction_id'].isin(company_ledger_df['transaction_id'])]

# Step 3: Find mismatched entries (those with the same transaction_id but different amounts)
mismatched = pd.merge(company_ledger_df, bank_transactions_df, on='transaction_id', how='inner', suffixes=('_ledger', '_bank'))
mismatched = mismatched[mismatched['amount_ledger'] != mismatched['amount_bank']]

# Replace NaN values with 0 in mismatched dataframe
mismatched.fillna(0, inplace=True)

# Convert date columns to string to avoid JSON serialization issues
missing_in_bank['date'] = missing_in_bank['date'].astype(str)
missing_in_ledger['date'] = missing_in_ledger['date'].astype(str)
mismatched['date_ledger'] = mismatched['date_ledger'].astype(str)
mismatched['date_bank'] = mismatched['date_bank'].astype(str)

# Displaying the reconciliation results
print("Missing in Bank:\n", missing_in_bank)
print("\nMissing in Ledger:\n", missing_in_ledger)
print("\nMismatched Transactions:\n", mismatched)

# Google Sheets API Setup
# Loading Google Sheets API credentials
creds = Credentials.from_service_account_file('credentials.json')

# Initializing the Sheets API
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

# Google Sheets ID 
SPREADSHEET_ID = '1catTToIncdIFNxMybvoC3y0HK4HbsuXuycLGELXt7Qs'

# Preparing data for exporting (header and data rows)
values = [
    ["Transaction ID", "Date", "Amount", "Source"],  # Headers
]

# Adding missing in bank to the values list
for index, row in missing_in_bank.iterrows():
    values.append([row['transaction_id'], row['date'], row['amount'], 'Missing in Bank'])

# Adding missing in ledger to the values list
for index, row in missing_in_ledger.iterrows():
    values.append([row['transaction_id'], row['date'], row['amount'], 'Missing in Ledger'])

# Adding mismatched transactions to the values list
for index, row in mismatched.iterrows():
    values.append([row['transaction_id'], row['date_ledger'], row['amount_ledger'], 'Mismatched in Ledger'])
    values.append([row['transaction_id'], row['date_bank'], row['amount_bank'], 'Mismatched in Bank'])

# Preparing the body for sending data to Google Sheets
body = {'values': values}

# Writing the data to the first sheet, starting from cell A1
result = sheet.values().update(
    spreadsheetId=SPREADSHEET_ID,
    range='Sheet1!A1',
    valueInputOption='RAW',
    body=body
).execute()
print(f"{result.get('updatedCells')} cells updated in Google Sheets.")