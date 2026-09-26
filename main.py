from storage import load_expenses
from services import (
    add_expense,
    search_expenses,
    update_expense,
    delete_expense,
    filter_expenses,
    expense_summary,
)
from models import Expense


def display_expenses(expenses: list[Expense]) -> None:
    if not expenses:
        print("No expenses found.")
        return

    print("======================================")
    print("            ALL EXPENSES              ")
    print("======================================")
    print("ID   Description   Amount   Category")

    for expense in expenses:
        print(
            f"{expense['id']}   "
            f"{expense['description']}   "
            f"{expense['amount']}   "
            f"{expense['category']}"
        )

            
def show_menu() -> None:

    print("======================================")
    print("         PERSONAL EXPENSE TRACKER     ")
    print("======================================")
    print(
        "1. Add Expense\n"
        "2. View Expenses\n"
        "3. Update Expense\n"
        "4. Delete Expense\n"
        "5. Search Expenses\n"
        "6. Filter Expenses\n"
        "7. Expense Summary\n"
        "8. Exit"
    )

def main():
    expenses = load_expenses()

    next_id = 1

    if expenses:
        next_id = max(expense["id"] for expense in expenses) + 1

    categories = [
        'Food',
        'Transport',
        'Shopping',
        'Bills',
        'Entertainment',
        'Health',
        'Education',
        'Other',
    ]

    while True:
        show_menu()
        user_choice = input("Please enter your choice: ")

        if user_choice == "1":
            next_id = add_expense(expenses, next_id, categories)
        elif user_choice == "2":
            display_expenses(expenses)
        elif user_choice == "3":
            update_expense(expenses, categories)
        elif user_choice == "4":
            delete_expense(expenses)
        elif user_choice == "5":
            search_expenses(expenses)
        elif user_choice == "6":
            filter_expenses(expenses, categories)
        elif user_choice == "7":
            expense_summary(expenses)
        elif user_choice == "8":
            print("Thank you for using Personal Expense Tracker!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")


if __name__ == "__main__":
    main()