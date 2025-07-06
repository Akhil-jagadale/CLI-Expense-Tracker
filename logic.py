import json
import os
import csv
from datetime import datetime

# Handle both direct execution and package imports
try:
    from aws_handler import upload_to_s3, log_to_cloudwatch
except ImportError:
    from .aws_handler import upload_to_s3, log_to_cloudwatch

# rest of your logic.py code...

# rest of your logic.py code...

EXPENSE_FILE = "data/expenses.csv"


def add_expense(amount, category, description, date=None):
    # Create the 'data' directory if it doesn't exist
    if not os.path.exists("data"):
        os.makedirs("data")

    # Use current date if none provided
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d")

    # Check if the file exists, if not, write the header
    file_exists = os.path.isfile(EXPENSE_FILE)

    with open(EXPENSE_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Amount", "Category", "Description", "Date"])
        writer.writerow([amount, category, description, date])

    log_to_cloudwatch(f"Added expense: Amount={amount}, Category={category}, Description={description}, Date={date}")

    if upload_to_s3(EXPENSE_FILE):
        print("Expense added and uploaded to S3 successfully.")
    else:
        print("Expense added, but failed to upload to S3.")


def view_expenses():
    if not os.path.exists(EXPENSE_FILE):
        print("No expenses recorded yet.")
        return

    with open(EXPENSE_FILE, mode="r") as file:
        reader = csv.reader(file)
        header = next(reader, None)
        if header:
            print(f"{'Index':<5} {header[0]:<10} {header[1]:<15} {header[2]:<20} {header[3]:<12}")
            print("-" * 65)

        for index, row in enumerate(reader):
            print(f"{index:<5} {row[0]:<10} {row[1]:<15} {row[2]:<20} {row[3]:<12}")

    log_to_cloudwatch("Viewed expenses.")


def delete_expense(index):
    expenses = []
    try:
        with open(EXPENSE_FILE, mode="r") as file:
            reader = csv.reader(file)
            header = next(reader)
            expenses = list(reader)
    except FileNotFoundError:
        print("No expenses recorded yet.")
        return

    if 0 <= index < len(expenses):
        deleted_expense = expenses[index]
        del expenses[index]

        with open(EXPENSE_FILE, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Amount", "Category", "Description", "Date"])
            writer.writerows(expenses)

        log_to_cloudwatch(f"Deleted expense at index {index}: {deleted_expense}")

        if upload_to_s3(EXPENSE_FILE):
            print(f"Expense at index {index} deleted and updated file uploaded to S3 successfully.")
        else:
            print(f"Expense at index {index} deleted, but failed to upload updated file to S3.")
    else:
        print(f"Invalid index. Please choose between 0 and {len(expenses) - 1}.")