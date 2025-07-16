from datetime import datetime

try:
    from logic import add_expense, view_expenses, delete_expense
except ImportError:
    from .logic import add_expense, view_expenses, delete_expense


def get_all_inputs():
    """Get all inputs in one go - command, then all required parameters"""
    print("\n=== Expense Tracker ===")
    print("Commands: add, view, delete, exit")

    while True:
        command = input("Enter command: ").strip().lower()
        if command in ['add', 'view', 'delete', 'exit']:
            return command
        else:
            print("Invalid command. Please enter: add, view, delete, or exit")


def get_add_inputs():
    """Get all inputs for adding expense in sequence"""
    print("\n--- Adding New Expense ---")

    # Get amount
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                print("Amount must be positive.")
                continue
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")

    # Get category
    while True:
        category = input("Enter category: ").strip()
        if category:
            break
        print("Category is required.")

    # Get description
    while True:
        description = input("Enter description: ").strip()
        if description:
            break
        print("Description is required.")

    # Get date (mandatory)
    while True:
        date = input("Enter date (YYYY-MM-DD): ").strip()
        if not date:
            print("Date is required.")
            continue
        try:
            datetime.strptime(date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    return amount, category, description, date


def get_delete_input():
    """Get index for deletion"""
    print("\n--- Deleting Expense ---")

    while True:
        try:
            index = int(input("Enter expense index to delete: "))
            if index < 0:
                print("Index must be non-negative.")
                continue
            return index
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    """Main function with sequential input collection"""
    print("Welcome to Expense Tracker!")
    print("All inputs are mandatory and will be collected sequentially.")

    while True:
        try:
            command = get_all_inputs()

            if command == "add":
                amount, category, description, date = get_add_inputs()
                add_expense(amount, category, description, date)
                print("✓ Expense added successfully!")

            elif command == "view":
                print("\n--- Your Expenses ---")
                view_expenses()

            elif command == "delete":
                # First show expenses, then get index
                print("\n--- Current Expenses ---")
                view_expenses()
                index = get_delete_input()
                delete_expense(index)
                print("✓ Expense deleted successfully!")

            elif command == "exit":
                print("Goodbye!")
                break

        except KeyboardInterrupt:
            print("\n\nOperation cancelled.")
            break
        except Exception as e:
            print(f"Error: {e}")
            continue


if __name__ == "__main__":
    main()
