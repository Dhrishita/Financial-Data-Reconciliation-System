# Financial-Data-Reconciliation-System
This tool automates the process of reconciling transactions between a company ledger and bank transactions, highlighting discrepancies and exporting results to Google Sheets.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#codestructure)
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


6. The system will start and wait for someone to stand in front of the camera. If the face is recognized, access will be granted. If the face is not recognized, an email with an OTP and the photo of the individual will be sent to the owner's email.

## Code Structure
- 'main.py': The main script to run the face recognition system.
- 'face_recognition.py': Contains the face recognition logic using OpenCV.
- 'email_notification.py': Handles sending email notifications for unrecognized faces.
- 'utils.py': Utility functions for the system.

## Contact
If you have any questions or suggestions, feel free to open an issue or contact:
Dhrishita Parve: dhrishitap18@gmail.com



