from src.file_manager import load_expenses, save_expenses
from src.expense import Expense
from src.utils import validate_amount, validate_date
from src.reports import total_expense, category_summary

def show_menu():
    print("\nPERSONAL FINANCE MANAGER")
    print("1. Add Expense")
    print("2. View Summary")
    print("3. Exit")

def run_app():
    expenses = load_expenses()

    while True:
        show_menu()
        choice = input("Enter choice: ")

        if choice == "1":
            amount = input("Amount: ")
            if not validate_amount(amount):
                print("Invalid amount")
                continue

            category = input("Category: ")
            date = input("Date (YYYY-MM-DD): ")
            if not validate_date(date):
                print("Invalid date")
                continue

            desc = input("Description: ")
            expenses.append(Expense(amount, category, date, desc))
            save_expenses(expenses)
            print("✅ Expense Added")

        elif choice == "2":
            print("Total:", total_expense(expenses))
            print("Category-wise:", category_summary(expenses))

        elif choice == "3":
            print("Goodbye 👋")
            break
