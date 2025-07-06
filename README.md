# Expense Tracker CLI

A command-line application for tracking expenses with AWS S3 storage and CloudWatch logging.

## Features
- Add, view, and delete expenses
- Automatic backup to AWS S3
- Activity logging to CloudWatch
- CSV data export
- Comprehensive testing

## Prerequisites
- Python 3.9+
- AWS Account with S3 and CloudWatch access
- boto3 library

## Setup
1. Clone repository
2. Install dependencies: `pip install -r requirements.txt`
3. Configure AWS credentials
4. Set environment variables:
   - `S3_BUCKET_NAME`
   - `CLOUDWATCH_LOG_GROUP_NAME`
   - `AWS_ACCESS_KEY_ID`
   - `AWS_SECRET_ACCESS_KEY`
   - `AWS_DEFAULT_REGION`

## Usage
```bash
# Add expense
python cli.py add 25.50 "Food" "Grocery shopping" --date 2024-01-15

# View all expenses
python cli.py view

# Delete expense by index
python cli.py delete 0
