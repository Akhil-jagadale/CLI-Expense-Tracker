import argparse
import sys
try:
    from logic import add_expense, view_expenses, delete_expense
except ImportError:
    from .logic import add_expense, view_expenses, delete_expense


def main():
    parser = argparse.ArgumentParser(description="Expense Tracker CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add Expense Command
    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("amount", type=float, help="Expense amount")
    add_parser.add_argument("category", type=str, help="Expense category")
    add_parser.add_argument("description", type=str, help="Expense description")
    add_parser.add_argument("--date", type=str, help="Expense date (YYYY-MM-DD)", required=False)

    # View Expenses Command
    view_parser = subparsers.add_parser("view", help="View expenses")

    # Delete Expense Command
    delete_parser = subparsers.add_parser("delete", help="Delete an expense")
    delete_parser.add_argument("index", type=int, help="Index of the expense to delete")

    args = parser.parse_args()

    try:
        if args.command == "add":
            add_expense(args.amount, args.category, args.description, args.date)
        elif args.command == "view":
            view_expenses()
        elif args.command == "delete":
            delete_expense(args.index)
        else:
            parser.print_help()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()