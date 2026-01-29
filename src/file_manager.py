import csv
from src.expense import Expense

def load_expenses(filename="data/expenses.csv"):
    expenses = []
    try:
        with open(filename, newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append(
                    Expense(
                        row["Amount"],
                        row["Category"],
                        row["Date"],
                        row["Description"]
                    )
                )
    except FileNotFoundError:
        print("⚠️ Expense file not found. Starting fresh.")
    return expenses


def save_expenses(expenses, filename="data/expenses.csv"):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount", "Description"])
        for exp in expenses:
            writer.writerow([exp.date, exp.category, exp.amount, exp.description])
