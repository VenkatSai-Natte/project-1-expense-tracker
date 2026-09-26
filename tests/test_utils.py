from utils import(
    get_description,
    get_amount,
    get_category,
)


def test_get_description(monkeypatch, capsys):
    inputs = iter(["", "Lunch"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = get_description()

    assert result == "Lunch"

    captured = capsys.readouterr()

    assert "Description cannot be empty." in captured.out


def test_get_amount(monkeypatch, capsys):

    inputs = iter(["abc", "-20", "200"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = get_amount()

    assert result == 200

    captured = capsys.readouterr()

    assert "Invalid amount" in captured.out
    assert "Amount must be greater than 0." in captured.out


def test_get_category(monkeypatch, capsys):

    categories = ['Food','Transport','Shopping','Bills','Entertainment','Health',
    'Education','Other']

    inputs = iter(["abc", "food"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = get_category(categories)

    assert result == "Food"

    captured = capsys.readouterr()

    assert "Invalid category." in captured.out