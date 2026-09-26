# Personal Expense Tracker

A command-line personal expense tracker built with Python. This project was created to practice Python fundamentals, modular application design, input validation, JSON persistence, type hints, and automated testing.

## Overview

The Personal Expense Tracker is a CLI application that allows users to manage their personal expenses.

Users can:

- Add expenses
- View all expenses
- Update existing expenses
- Delete expenses
- Search expenses by description
- Filter expenses by category
- Filter expenses by amount range
- View an expense summary
- Persist expense data using a JSON file

The application validates user input and stores expense data locally so that the data is available when the application is restarted.

## Features

### Expense Management

- Add a new expense
- Automatically assign a unique expense ID
- View all expenses
- Update an existing expense
- Delete an existing expense

### Search

- Search expenses using a description
- Case-insensitive search
- Supports partial description matching
- Displays multiple matching expenses

### Filtering

- Filter expenses by category
- Filter expenses by minimum and maximum amount
- Validates that the minimum amount is not greater than the maximum amount

### Expense Summary

The application provides:

- Total number of expenses
- Total amount spent
- Total amount spent by category
- Percentage of total spending for each category

### Input Validation

The application validates:

- Empty descriptions
- Invalid amounts
- Zero or negative amounts
- Invalid categories
- Invalid expense IDs
- Invalid menu choices
- Invalid filter choices
- Invalid amount ranges

### Data Persistence

Expense data is stored locally using JSON.

The application:

1. Loads existing expenses when it starts.
2. Saves changes when expenses are added, updated, or deleted.

## Technologies Used

- Python
- JSON
- pathlib
- pytest
- Git

## Python Concepts Practiced

This project was used to practice the following Python concepts:

- Variables and data types
- Strings
- Lists
- Dictionaries
- Loops
- Conditional statements
- Functions
- Function parameters and return values
- Type hints
- TypedDict
- List and dictionary operations
- Exception handling
- try / except
- while loops
- Modules and imports
- File handling
- JSON serialization and deserialization
- pathlib.Path
- Generator expressions
- max()
- Separation of responsibilities
- Automated testing

## Project Structure

    project_1_expense_tracker/
    │
    ├── main.py
    ├── models.py
    ├── services.py
    ├── storage.py
    ├── utils.py
    │
    ├── tests/
    │   ├── test_storage.py
    │   ├── test_services.py
    │   └── test_utils.py
    │
    ├── data/
    │   └── expenses.json
    │
    ├── .gitignore
    └── README.md

## Module Responsibilities

### main.py

Responsible for the application flow.

It:

- Loads expenses when the application starts
- Displays the main menu
- Reads the user's menu choice
- Calls the appropriate service function
- Maintains the application's main state
- Determines the next expense ID

### models.py

Contains the Expense TypedDict.

It defines the expected structure of an expense:

    class Expense(TypedDict):
        id: int
        description: str
        amount: int
        category: str

### services.py

Contains the application's expense-related business logic.

It handles:

- Adding expenses
- Searching expenses
- Updating expenses
- Deleting expenses
- Filtering expenses
- Generating expense summaries

### utils.py

Contains reusable functions for user input and validation.

It handles:

- Description validation
- Amount validation
- Category validation

### storage.py

Responsible for JSON file persistence.

It provides functions for:

- Saving expenses
- Loading expenses

### tests/

Contains automated tests written using pytest.

Tests cover:

- Utility functions
- Expense services
- JSON storage

### data/expenses.json

Stores the application's expense data.

## Requirements

The project requires:

- Python 3.x
- pytest

Python can be downloaded from:

https://www.python.org/

pytest can be installed using:

    python -m pip install pytest

## How to Run the Application

Open a terminal in the project directory:

    cd path\to\project_1_expense_tracker

Run:

    python main.py

## Application Menu

The application provides the following menu:

    ======================================
             PERSONAL EXPENSE TRACKER
    ======================================
    1. Add Expense
    2. View Expenses
    3. Update Expense
    4. Delete Expense
    5. Search Expenses
    6. Filter Expenses
    7. Expense Summary
    8. Exit

## Example

### Adding an Expense

Example input:

    Enter expense description: Lunch
    Enter amount: 200
    Enter category: Food

The application adds the expense and assigns an ID automatically.

Example:

    ID   Description   Amount   Category
    1    Lunch         200     Food

### Searching Expenses

The user can search using part of an expense description.

For example:

    Enter search term: lunch

The search is case-insensitive and can return multiple matching expenses.

### Filtering by Category

The user can select a category such as:

    Food

and view expenses belonging to that category.

### Filtering by Amount

The user can specify a minimum and maximum amount.

For example:

    Minimum amount: 100
    Maximum amount: 300

The application displays expenses within that range.

### Expense Summary

The summary displays information such as:

    ======================================
               EXPENSE SUMMARY
    ======================================

    Total Expenses : 3
    Total Amount   : 470

    Category Breakdown:

    Food          : 350 (74.47%)
    Transport     : 120 (25.53%)

## Data Persistence

The application uses JSON for local data persistence.

The data is stored in:

    data/expenses.json

For example:

    [
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

When the application starts, existing expenses are loaded from the JSON file.

When an expense is added, updated, or deleted, the JSON file is updated.

## Testing

The project uses pytest for automated testing.

Run all tests with:

    python -m pytest

The current test suite contains 19 tests covering:

- Description validation
- Amount validation
- Category validation
- Adding expenses
- Searching expenses
- Updating expenses
- Deleting expenses
- Filtering by category
- Filtering by amount
- Invalid amount ranges
- Expense summaries
- Empty summaries
- JSON save/load operations
- Empty JSON data

Expected result:

    19 passed

## Testing Techniques Practiced

This project also provides practice with pytest features such as:

### assert

Used to verify expected results:

    assert result == "Lunch"

### monkeypatch

Used to replace input() during tests:

    monkeypatch.setattr(
        "builtins.input",
        lambda _: "Lunch"
    )

This allows interactive functions to be tested automatically.

### capsys

Used to capture console output:

    captured = capsys.readouterr()

    assert "Expense not found." in captured.out

### tmp_path

Used to create temporary files for storage tests without modifying the application's real data file.

## Architecture

The application separates different responsibilities into different modules.

    main.py
       │
       ▼
    services.py
       /       \
      ▼         ▼
    utils.py  storage.py
                   │
                   ▼
             expenses.json

    models.py
       │
       ▼
    Expense TypedDict

### Responsibility Separation

    main.py
        → Application flow

    services.py
        → Business logic

    utils.py
        → Input and validation

    storage.py
        → Data persistence

    models.py
        → Data structure/type definition

    tests/
        → Automated testing

This separation makes the application easier to understand, test, and maintain.

## Error Handling

The application handles common invalid inputs without crashing.

Examples include:

    Invalid amount. Please enter a number.

    Amount must be greater than 0.

    Description cannot be empty.

    Invalid category.

    Expense not found.

The application continues asking for valid input when appropriate.

## Git

Git is used for version control.

The project contains a .gitignore file to prevent generated or environment-specific files from being tracked.

Examples include:

    __pycache__/
    *.pyc
    .pytest_cache/
    .venv/
    venv/
    .env
    .vscode/

The project can be initialized as a Git repository using:

    git init

Check repository status with:

    git status

## Learning Outcomes

Through this project, the following practical development skills were practiced:

- Building a Python CLI application
- Structuring an application across multiple modules
- Writing reusable functions
- Using type hints
- Defining structured dictionary types with TypedDict
- Validating user input
- Handling exceptions
- Reading and writing JSON files
- Using pathlib
- Designing basic business logic
- Writing automated tests
- Using pytest fixtures and utilities
- Testing functions that use user input
- Testing console output
- Testing file persistence safely
- Using Git for version control
- Writing basic project documentation

## Future Improvements

Possible future enhancements include:

- Better formatted expense tables
- Expense budgets
- Monthly expense reports
- Date support for expenses
- Export to CSV
- More advanced reporting
- Database persistence
- REST API implementation
- Authentication and authorization

These features are intentionally outside the current scope of this beginner-level project.

## Project Status

The current version of the project includes:

- Expense CRUD operations
- Search
- Filtering
- Expense summaries
- JSON persistence
- Input validation
- Modular code structure
- Automated tests
- Git configuration
- Project documentation

All current automated tests are passing.

## License

This project was created as a personal learning project and does not currently use a specific open-source license.