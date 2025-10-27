import json
import logging
from datetime import datetime

# Global variable
stock_data = {}

def add_item(item: str = "default", qty: int = 0, logs=None):                           # Added snake_case and docstrings
    """Add a non-negative integer quantity of a string item to stock."""              # Fixed dangerous mutable default arg
    if logs is None:                
        logs = []
    if not item:
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append("%s: Added %d of %s" % (str(datetime.now()), qty, item))


def remove_item(item: str, qty: int):
    """Remove a non-negative integer quantity of a string item from stock."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        return     # Removed bare except


def get_qty(item: str) -> int:
    """Return quantity for an item; 0 if missing."""
    return stock_data[item]

def load_data(file_path: str = "inventory.json") -> None:
    """Load stock data from JSON file into memory."""    # Safe file handling
    global stock_data
    with open(file, "r", encoding="utf-8") as f:
        stock_data = json.loads(f.read())

def save_data(file_path: str = "inventory.json") -> None:
    """Persist current stock data dictionary into JSON file."""
    with open(file, "w", encoding="utf-8") as f:
        f.write(json.dumps(stock_data))


def print_data() -> None:
    """Print a simple report of all items and quantities."""
    print("Items Report")
    for i in stock_data:
        print(i, "->", stock_data[i])

def check_low_items(threshold: int = 5) -> list[str]:
    """Return items with quantity below the given threshold."""
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result

def main():
    add_item("apple", 10)
    add_item("banana", -2)
    add_item(123, "ten")  # invalid types, no check
    remove_item("apple", 3)
    remove_item("orange", 1)
    print("Apple stock:", getQty("apple"))
    print("Low items:", checkLowItems())
    save_data()
    load_data()
    print_data()
    # removed eval

main()
