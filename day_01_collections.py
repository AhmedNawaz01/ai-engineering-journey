transactions = [
    {
        "id": 1,
        "amount": 1200,
        "category": "food"
    },
    {
        "id": 2,
        "amount": 2500,
        "category": "rent"
    },
    {
        "id": 3,
        "amount": 450,
        "category": "transport"
    },
    {
        "id": 4,
        "amount": 800,
        "category": "food"
    },
    {
        "id": 5,
        "amount": 150,
        "category": "shopping"
    },
    {
        "id": 6,
        "amount": 300,
        "category": "transport"
    }
]

def calculate_total_transactions(transactions: list[dict[str, int | str]]) -> int:
    return len(transactions)

def calculate_total_transactions_amount(transactions:list) -> float:
    total = 0
    for transaction in transactions:
        total += transaction["amount"]
    return total

def find_unique_categories(transactions:list) -> set[str]:
    categories = set()
    for transaction in transactions:
        categories.add(transaction["category"])
    return categories

def count_transactions_above(transactions: list, minimum_amount: int) -> int:
    filtered_transactions = [
        transaction
        for transaction in transactions
        if transaction["amount"] > minimum_amount
    ]
    return len(filtered_transactions)


def transaction_category_summary(transactions:list):
    transactions_summary = {}
    for transaction in transactions:
        category = transaction["category"]
        amount = transaction["amount"]
        if category not in transactions_summary:
            transactions_summary[category] = 0
        transactions_summary[category] += amount
    return transactions_summary

def find_highest_transaction(transactions: list) -> dict | None:
    if not transactions:
        return None
    highest = transactions[0]
    for transaction in transactions:
        if transaction["amount"] > highest["amount"]:
            highest = transaction
    return highest

def filter_by_category(transactions: list, category: str) -> list:
    filtered_list = []
    for transaction in transactions:
        if transaction["category"] == category:
            filtered_list.append(transaction)
    return filtered_list

print(f"Total transaction: {calculate_total_transactions(transactions)}.")
print(f"Total amount: {calculate_total_transactions_amount(transactions)}.")
print(f"Unique categories: {find_unique_categories(transactions)}.")
print(f"Transactions having amount more than 500: {count_transactions_above(transactions, 500)}")
print(f"Highest transaction: {find_highest_transaction(transactions)}")
print(f"Food transactions: {filter_by_category(transactions, 'food')}")
print(f"Transaction category summary: {transaction_category_summary(transactions)}.")

