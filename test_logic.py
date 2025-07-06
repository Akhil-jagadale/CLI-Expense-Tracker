import pytest
import os
import csv
from unittest.mock import patch
from expense_tracker.logic import add_expense, view_expenses, delete_expense

EXPENSE_FILE = "data/expenses.csv"


@pytest.fixture(autouse=True)
def setup_expense_file():
    # Ensure the data directory exists
    if not os.path.exists("data"):
        os.makedirs("data")

    # Clean up the expense file before each test
    if os.path.exists(EXPENSE_FILE):
        os.remove(EXPENSE_FILE)

    yield

    # Clean up after test
    if os.path.exists(EXPENSE_FILE):
        os.remove(EXPENSE_FILE)


@patch('expense_tracker.logic.upload_to_s3')
@patch('expense_tracker.logic.log_to_cloudwatch')
def test_add_expense(mock_log, mock_upload):
    mock_upload.return_value = True
    mock_log.return_value = True

    add_expense(10.0, "Food", "Lunch", "2024-01-01")

    with open(EXPENSE_FILE, mode="r") as file:
        reader = csv.reader(file)
        rows = list(reader)
        assert len(rows) == 2  # Header + 1 expense
        assert rows[1] == ["10.0", "Food", "Lunch", "2024-01-01"]


@patch('expense_tracker.logic.log_to_cloudwatch')
def test_view_expenses(mock_log, capsys):
    mock_log.return_value = True

    # Create a test file with expenses
    with open(EXPENSE_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Amount", "Category", "Description", "Date"])
        writer.writerow(["20.0", "Travel", "Train ticket", "2024-01-02"])

    view_expenses()
    captured = capsys.readouterr()
    assert "20.0" in captured.out
    assert "Travel" in captured.out


@patch('expense_tracker.logic.upload_to_s3')
@patch('expense_tracker.logic.log_to_cloudwatch')
def test_delete_expense(mock_log, mock_upload):
    mock_upload.return_value = True
    mock_log.return_value = True

    # Create a test file with expenses
    with open(EXPENSE_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Amount", "Category", "Description", "Date"])
        writer.writerow(["30.0", "Entertainment", "Movie", "2024-01-03"])

    delete_expense(0)

    with open(EXPENSE_FILE, mode="r") as file:
        reader = csv.reader(file)
        rows = list(reader)
        assert len(rows) == 1  # Only header should remain