from services import(
    search_expenses,
    add_expense,
    update_expense,
    delete_expense,
    filter_expenses,
    expense_summary,
)

def test_search_expenses(monkeypatch, capsys):
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
        },
        {
            "id": 3,
            "description": "Lunch",
            "amount": 300,
            "category": "Food"
        }
    ]

    monkeypatch.setattr("builtins.input", lambda _: "Lunch")

    search_expenses(expenses)

    captured = capsys.readouterr()

    assert "Lunch" in captured.out
    assert "200" in captured.out
    assert "300" in captured.out
    assert "Uber" not in captured.out


def test_add_expense(monkeypatch):
    inputs = iter(["Lunch", "200", "Food"])
    expenses = []
    next_id = 1
    categories = ["Food", "Transport", "Shopping"]

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    monkeypatch.setattr("services.save_expenses", lambda expenses: None)

    next_id = add_expense(expenses, next_id, categories)

    assert next_id == 2
    assert len(expenses) == 1
    assert expenses[0]["id"] == 1
    assert expenses[0]["description"] == "Lunch"
    assert expenses[0]["amount"] == 200
    assert expenses[0]["category"] == "Food"


def test_update_expense(monkeypatch, capsys):
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
        },
        {
            "id": 3,
            "description": "Lunch",
            "amount": 300,
            "category": "Food"
        }
    ]

    categories = ['Food','Transport','Shopping','Bills','Entertainment','Health',
    'Education','Other']

    inputs = iter(["3", "Go Karting", "500", "Entertainment"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    monkeypatch.setattr("services.save_expenses", lambda expenses: None)

    update_expense(expenses, categories)

    captured = capsys.readouterr()

    assert expenses[2]["id"] == 3
    assert expenses[2]["description"] == "Go Karting"
    assert expenses[2]["amount"] == 500
    assert expenses[2]["category"] == "Entertainment"
    assert "Expense ID 3 updated successfully." in captured.out
    assert "Expense not found" not in captured.out

def test_update_expense_invalid_and_not_found(monkeypatch, capsys):
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
        },
        {
            "id": 3,
            "description": "Lunch",
            "amount": 300,
            "category": "Food"
        }
    ]

    categories = ['Food','Transport','Shopping','Bills','Entertainment','Health',
    'Education','Other']

    inputs = iter(["abc", "99"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    update_expense(expenses, categories)

    captured = capsys.readouterr()

    assert "Invalid" in captured.out
    assert "Expense not found" in captured.out


def test_delete_expense(monkeypatch, capsys):
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
        },
        {
            "id": 3,
            "description": "Lunch",
            "amount": 300,
            "category": "Food"
        }
    ]

    inputs = iter(["3"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    monkeypatch.setattr("services.save_expenses", lambda expenses: None)

    delete_expense(expenses)

    captured = capsys.readouterr()

    assert len(expenses) == 2
    for expense in expenses:
        assert expense["id"] != 3
    assert "Expense ID 3 deleted successfully." in captured.out


def test_delete_invalid_and_not_found_expense(monkeypatch, capsys):
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
        },
        {
            "id": 3,
            "description": "Lunch",
            "amount": 300,
            "category": "Food"
        }
    ]

    inputs = iter(["abc", "100"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    delete_expense(expenses)

    captured = capsys.readouterr()

    assert "Invalid expense ID" in captured.out
    assert "Expense not found" in captured.out


def test_filter_by_category(monkeypatch, capsys):
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
        },
        {
            "id": 3,
            "description": "Lunch",
            "amount": 150,
            "category": "Food"
        }
    ]

    categories = ['Food','Transport','Shopping','Bills','Entertainment','Health',
    'Education','Other']

    inputs = iter(["1", "Food", "3"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    filter_expenses(expenses, categories)

    captured = capsys.readouterr()

    assert "Food" in captured.out
    assert "200" in captured.out
    assert "150" in captured.out
    assert "Uber" not in captured.out


def test_filter_category_not_found(monkeypatch, capsys):
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
        },
        {
            "id": 3,
            "description": "Lunch",
            "amount": 150,
            "category": "Food"
        }
    ]

    categories = ['Food','Transport','Shopping','Bills','Entertainment','Health',
    'Education','Other']

    inputs = iter(["1", "Bills", "3"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    filter_expenses(expenses, categories)

    captured = capsys.readouterr()

    assert "Expenses not found for the given category" in captured.out
    assert "Lunch" not in captured.out


def test_filter_by_amount(monkeypatch, capsys):
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
        },
        {
            "id": 3,
            "description": "Lunch",
            "amount": 150,
            "category": "Food"
        }
    ]

    categories = ['Food','Transport','Shopping','Bills','Entertainment','Health',
    'Education','Other']

    inputs = iter(["2", "120", "200", "3"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    filter_expenses(expenses, categories)

    captured = capsys.readouterr()

    assert "150" in captured.out
    assert "200" in captured.out
    assert "120" in captured.out
    assert "Uber" in captured.out


def test_filter_by_amount_invalid_input(monkeypatch, capsys):
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
        },
        {
            "id": 3,
            "description": "Lunch",
            "amount": 150,
            "category": "Food"
        }
    ]

    categories = ['Food','Transport','Shopping','Bills','Entertainment','Health',
    'Education','Other']

    inputs = iter(["2", "abc","120","200", "3"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    filter_expenses(expenses, categories)

    captured = capsys.readouterr()

    assert "Invalid amount" in captured.out
    assert "150" in captured.out
    assert "200" in captured.out
    assert "120" in captured.out


def test_filter_invalid_amount_range(monkeypatch, capsys):
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
        },
        {
            "id": 3,
            "description": "Lunch",
            "amount": 150,
            "category": "Food"
        }
    ]

    categories = ['Food','Transport','Shopping','Bills','Entertainment','Health',
    'Education','Other']

    inputs = iter(["2", "220", "200", "200", "220", "3"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    filter_expenses(expenses, categories)

    captured = capsys.readouterr()

    assert "Minimum amount cannot be greater than maximum amount." in captured.out
    assert "Lunch" in captured.out
    assert "200" in captured.out


def test_filter_amount_range_no_results(monkeypatch, capsys):
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
        },
        {
            "id": 3,
            "description": "Lunch",
            "amount": 150,
            "category": "Food"
        }
    ]

    categories = ['Food','Transport','Shopping','Bills','Entertainment','Health',
    'Education','Other']

    inputs = iter(["2", "300", "500", "120", "200", "3"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    filter_expenses(expenses, categories)

    captured = capsys.readouterr()

    assert "No expenses found in the given amount range." in captured.out


def test_expense_summary(capsys):
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
        },
        {
            "id": 3,
            "description": "Lunch",
            "amount": 150,
            "category": "Food"
        }
    ]

    expense_summary(expenses)

    captured = capsys.readouterr()

    assert "Total Expenses : 3" in captured.out
    assert "Total Amount   : 470" in captured.out
    assert "Food    : 350" in captured.out
    assert "Transport    : 120" in captured.out
    assert "74.47%" in captured.out
    assert "25.53%" in captured.out


def test_empty_expense_summary(capsys):
    expenses = []

    expense_summary(expenses)

    captured = capsys.readouterr()

    assert "No expenses found." in captured.out