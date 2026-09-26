from utils import (
    get_description,
    get_amount,
    get_category,
)
from storage import save_expenses
from models import Expense


def add_expense(
    expenses: list[Expense],
    next_id: int,
    categories: list[str],
) -> int:
    expense = {
        "id": next_id,
        "description": get_description(),
        "amount": get_amount(),
        "category": get_category(categories),
    }
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!")
    return next_id + 1
    

def search_expenses(expenses: list[Expense]) -> None:
    search_term = input("Enter search term: ").lower().strip()
    found_expense = False
    for expense in expenses:
        if search_term in expense["description"].lower():
            if not found_expense:
                print("ID   Description   Amount   Category")
            print(f"{expense['id']}   {expense['description']}   {expense['amount']}   {expense['category']}")
            found_expense = True
    if not found_expense:
        print("No matching expenses found.")


def update_expense(
    expenses: list[Expense],
    categories: list[str],
) -> None:
    while True:
        try:
            expense_id = int(input("Enter expense ID to update: "))
            break
        except ValueError:
            print("Invalid expense ID. Please enter an integer.")
    expense_found = False
    for expense in expenses:
        if expense["id"] == expense_id:
            expense["description"] = get_description()
            expense["amount"] = get_amount()
            expense["category"] = get_category(categories)
            print(f"Expense ID {expense_id} updated successfully.")
            expense_found = True
            save_expenses(expenses)
            break
    if not expense_found:
        print("Expense not found.")


def delete_expense(expenses: list[Expense]) -> None:
    while True:
        try:
            expense_id = int(input("Enter expense ID to delete: "))
            break
        except ValueError:
            print("Invalid expense ID. Please enter an integer.")
    expense_found = False
    for expense in expenses:
        if expense["id"] == expense_id:
            expenses.remove(expense)
            print(f"Expense ID {expense_id} deleted successfully.")
            expense_found = True
            save_expenses(expenses)
            break
    if not expense_found:
        print("Expense not found.")


def filter_expenses(
    expenses: list[Expense], 
    categories: list[str],
) -> None:
    while True:
        print("1. Filter by Category\n2. Filter by Amount\n3. Back")
        filter_choice = input("Enter filter choice: ")
        found_expense = False

        if filter_choice == "1":
            filter_category = get_category(categories)
            for expense in expenses:
                if expense["category"] == filter_category:
                    if not found_expense:
                        print("ID   Description   Amount   Category")
                    print(
                        f"{expense['id']}   "
                        f"{expense['description']}   "
                        f"{expense['amount']}   "
                        f"{expense['category']}"
                    )
                    found_expense = True
            if not found_expense:
                print("Expenses not found for the given category")

        elif filter_choice == "2":
            while True:
                print("Minimum amount")
                minimum_amount = get_amount()
                print("maximum amount")
                maximum_amount = get_amount()
                if minimum_amount > maximum_amount:
                    print("Minimum amount cannot be greater than maximum amount.\nPlease enter the range again.")
                    continue
                for expense in expenses:
                    if minimum_amount <= expense["amount"] <= maximum_amount:
                        if not found_expense:
                            print("ID   Description   Amount   Category")
                        print(f"{expense['id']}   {expense['description']}   {expense['amount']}   {expense['category']}")
                        found_expense = True
                if found_expense:
                    break
                else:
                    print("No expenses found in the given amount range.")

        elif filter_choice == "3":
            break
        else:
            print("Invalid filter choice. Please enter 1, 2, or 3.")


def expense_summary(expenses: list[Expense]) -> None:
    print("======================================")
    print("           EXPENSE SUMMARY            ")
    print("======================================")

    if not expenses:
        print("No expenses found.")
        return

    total_amount = 0
    category_total: dict[str, int] = {}

    for expense in expenses:
        total_amount += expense["amount"]

        expense_category = expense["category"]

        if expense_category in category_total:
            category_total[expense_category] += expense["amount"]
        else:
            category_total[expense_category] = expense["amount"]

    print(f"Total Expenses : {len(expenses)}")
    print(f"Total Amount   : {total_amount}\n")

    print("Category Breakdown:")

    for category, amount in category_total.items():
        percentage = (amount / total_amount) * 100
        print(f"{category}    : {amount} ({percentage:.2f}%)")