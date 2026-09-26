def get_description() -> str:
    while True:
        description = input("Enter expense description: ").strip()
        if description == "":
            print("Description cannot be empty.")
        else:
            return description


def get_amount() -> int:
    while True:
        try:
            amount = int(input("Enter amount: "))
        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue
        if amount > 0:
            return amount
        else:
            print("Amount must be greater than 0.")


def get_category(categories: list[str]) -> str:
    while True:
        category = input("Enter category: ").strip()
        for allowed_category in categories:
            if allowed_category.lower() == category.lower():         
                return allowed_category
        print(f"Invalid category.\nPlease choose from:\n{categories}")