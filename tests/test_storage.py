from storage import save_expenses, load_expenses


def test_save_and_load_expenses(tmp_path):

    expenses = [
        {
            "id": 1,
            "description": "Lunch",
            "amount": 200,
            "category": "Food"
        },
        {
            "id": 2,
            "description": "Uber",
            "amount": 120,
            "category": "Transport"
        }
    ]

    test_file = tmp_path / "test_expenses.json"

    save_expenses(expenses, test_file)
    loaded_expenses = load_expenses(test_file)

    assert expenses == loaded_expenses

def test_save_and_load_empty_expenses(tmp_path):
    expenses = []

    test_file = tmp_path / "test_expenses.json"

    save_expenses(expenses, test_file)
    loaded_expenses = load_expenses(test_file)

    assert expenses == loaded_expenses