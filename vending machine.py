# Item class
class Item:
    def __init__(self, name, code, price, stock, category):
        self.name = name
        self.code = code
        self.price = price
        self.stock = stock
        self.category = category

    def __str__(self):
        return f"Item name: {self.name} | Code: {self.code} | Price: ${self.price:.2f} | Stock: {self.stock}"

# Category class
class Category:
    def __init__(self, name, items):
        self.name = name
        self.items = items

    def __str__(self):
        return f"Category: {self.name}"

# Print menu function
def print_menu(categories):
    print("Welcome to Manuel's Vending Machine")
    print("=" * 90)
    for category in categories:
        print(category)
        for item in category.items:
            print(item)
        print("=" * 90)

# Get item by code function
def get_item_by_code(categories, code):
    for category in categories:
        for item in category.items:
            if item.code == code:
                return item
    return None

# Dispense item function
def dispense_item(item):
    print(f"Dispensing {item.name}...")
    item.stock -= 1

# Calculate change function
def calculate_change(price, amount_paid):
    return round(amount_paid - price, 2)

# Buy item function
def buy_item(categories):
    code = input("Enter the code of the item you want: ")
    item = get_item_by_code(categories, code)
    if item is None:
        print("Invalid code. Please try again.")
        return
    price = item.price
    while True:
        try:
            amount_paid = float(input(f"Enter {price:.2f} dollars to purchase: "))
            if amount_paid < price:
                print("Insufficient funds. Please try again.")
            else:
                change = calculate_change(price, amount_paid)
                dispense_item(item)
                print(f"Thank you for your purchase! You have received {change:.2f} dollars in change.")
                return
        except ValueError:
            print("Invalid input. Please try again.")

# Main function
def main():
    chocolates = [
        Item("Snicker's bar", "A1", 2.95, 10, "Chocolates"),
        Item("KitKat bar", "A2", 1.95, 5, "Chocolates"),
        Item("M&ms", "A3", 3.25, 2, "Chocolates")
    ]
    soft_drinks = [
        Item("Coca Cola", "B1", 1.50, 10, "Soft Drinks"),
        Item("Pepsi", "B2", 1.50, 8, "Soft Drinks"),
        Item("Sprite", "B3", 1.50, 6, "Soft Drinks")
    ]
    snacks = [
        Item("Lays", "C1", 1.00, 15, "Chips"),
        Item("Doritos", "C2", 1.00, 10, "Chips"),
        Item("Cheetos", "C3", 1.00, 5, "Chips")
    ]
    hot_drinks = [
        Item("Coffee", "D1", 2.00, 20, "Hot Drinks"),
        Item("Tea", "D2", 1.50, 20, "Hot Drinks"),
        Item("Hot Chocolate", "D3", 2.50, 15, "Hot Drinks")
    ]
    noodles = [
        Item("Ramen", "E1", 3.00, 10, "Noodles"),
        Item("Udon", "E2", 3.50, 8, "Noodles"),
        Item("Soba", "E3", 3.50, 6, "Noodles")
    ]

    categories = [
        Category("Chocolates", chocolates),
        Category("Soft Drinks", soft_drinks),
        Category("Snacks", snacks),
        Category("Hot Drinks", hot_drinks),
        Category("Noodles", noodles)
    ]

    while True:
        print("Welcome to Manuel's Vending Machine")
        print("1. Buy an item")
        print("2. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            print_menu(categories)
            buy_item(categories)
        elif choice == "2":
            break
        else:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()
