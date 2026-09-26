import json
from pathlib import Path
from models import Expense

EXPENSE_FILE = Path(__file__).parent / "data/expenses.json"

def save_expenses(expenses: list[Expense], file_path: Path = EXPENSE_FILE) -> None:
    with open(file_path, "w") as file:
        json.dump(expenses, file, indent=4)


def load_expenses(file_path: Path = EXPENSE_FILE) -> list[Expense]:
    with open(file_path, "r") as file:
        expenses = json.load(file)
    return expenses