# Financial-Data-Reconciliation-System
This tool automates the process of reconciling transactions between a company ledger and bank transactions, highlighting discrepancies and exporting results to Google Sheets.

This README provides detailed steps for setting up the Google Sheets API, including creating a Google Cloud project, enabling the API, creating a service account, and sharing the Google Sheets spreadsheet. Adjust the sections and details further if needed to match your specific project setup and instructions.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Setup](#setup)
- [Contact](#contact)

## Introduction

This project connects to two MySQL databases (company_ledger_db and bank_transactions_db) to fetch transaction data. It identifies discrepancies such as missing transactions and mismatches in amounts between the two databases. Results are then exported to a Google Sheets spreadsheet using the Google Sheets API for further analysis and reporting.

## Features

- **Database Connection:** Connects to MySQL databases to fetch transactional data.
- **Data Reconciliation:** Identifies transactions missing in either the company ledger or bank transactions, as well as mismatches in amounts.
- **Google Sheets Integration:** Uses Google Sheets API to export reconciliation results for easy review and analysis.
- **Error Handling:** Handles various types of data discrepancies and ensures accurate reporting.

## Requirements
- Python 3.x
- MySQL Connector (mysql-connector-python)
- Pandas (pandas)
- Google API Python Client (google-api-python-client)
  
## Installation
## Setup
1. Clone this repository to your Raspberry Pi:
   
   ```bash
   git clone https://github.com/your-username/bank-reconciliation-tool.git
   cd bank-reconciliation-tool

2. Install dependencies:

   ```bash
   pip install -r requirements.txt

3. Setup MySQL:
   
- Ensure MySQL server is running.
- Create databases company_ledger_db and bank_transactions_db.
- Populate databases with transaction data.

4. Setup Google Sheets API:
   
- Create a Google Cloud Project:
  - Go to the Google Cloud Console and create a new project.
    
- Enable Google Sheets API:
  - In the Google Cloud Console, navigate to the **"APIs & Services" > "Library" section.**
  - Search for **"Google Sheets API"** and enable it for your project.
 
- Create Service Account:
  - Go to the Google Cloud Console and navigate to **"APIs & Services" > "Credentials".**
  - Click on **"Create credentials"** and select "Service account".
  - Fill in the details and click "Create".
  - Assign the **"Project" > "Editor"** role to the service account.
  - Download the JSON credentials file (credentials.json).
 
- Share Google Sheets Spreadsheet:
  - Create a new Google Sheets spreadsheet or use an existing one.
  - Share the spreadsheet with the email address associated with the service account (found in credentials.json).

5. Configure Credentials:

- Place the downloaded credentials.json file in the root directory of your project.

6. Run the script:

   ```bash
   python bank.py

7. View results:

- Check the Google Sheets spreadsheet (SPREADSHEET_ID) for reconciliation results.

## Contact
If you have any questions or suggestions, feel free to open an issue or contact:
Dhrishita Parve: dhrishitap18@gmail.com



