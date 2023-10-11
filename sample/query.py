
from data import stock
from datetime import datetime

def main():
    today = datetime.now()
    username = input("Enter your username: ")
    print(f"Hello, {username}! What would you like to do?")

    while True:
        print("1 - List items in stock")
        print("2 - Search an item and place an order")
        print("3 - Browse by category")
        print("4 - Quit")
        
        choice = input("Type the number of the operation: ")

        if choice == "1":
            list_items_in_stock(stock)
            count_items_in_warehouses(stock)
        elif choice == "2":
            search_and_order(stock)
        elif choice == "3":
            browse_by_category(stock)
        elif choice == "4":
            print(f"Thank you for your visit, {username}.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

def list_items_in_stock(stock):
    print("Items in stock:")
    for item in stock:
        print(f"{item['state']} {item['category']}")

def count_items_in_warehouses(stock):
    items_in_warehouse1 = 0
    items_in_warehouse2 = 0

    for item in stock:
        if item.get('warehouse') == 1:
            items_in_warehouse1 += 1
        elif item.get('warehouse') == 2:
            items_in_warehouse2 += 1

    print(f"Total items in warehouse 1: {items_in_warehouse1}")
    print(f"Total items in warehouse 2: {items_in_warehouse2}")

def search_and_order(stock):
    
    item_name = input("What is the name of the item? ").lower()
    total_available1 = 0  # Initialize counts for both warehouses
    total_available2 = 0

    for item in stock:
        if item_name.lower() in f"{item['state']} {item['category']}".lower():
            if item["warehouse"] == 1:
                total_available1 += 1
            elif item["warehouse"] == 2:
                total_available2 += 1

    total_available = total_available1 + total_available2

    if total_available == 0:
        print("Amount available: 0")
        print("Location: Not in stock")
    else:
        print(f"Amount available in Warehouse 1: {total_available1}")
        print(f"Amount available in Warehouse 2: {total_available2}")
        print(f"The total amount available of this item is: {total_available}")

    order = input("Would you like to order this item? (y/n) ").lower()

    if order == 'y':
        desired_amount = int(input("How many would you like? "))

        if desired_amount <= total_available:
            print(f"{desired_amount} {item_name} have been ordered.")
        else:
            print("There are not this many available.")
            order_max = input("Would you like to order the maximum available? (y/n) ").lower()

            if order_max == 'y':
                max_available = max(total_available1, total_available2)
                if max_available == total_available1:
                    print(f"{total_available1} {item_name} have been ordered from Warehouse 1.")
                else:
                    print(f"{total_available2} {item_name} have been ordered from Warehouse 2.")
            else:
                print(f"{desired_amount} {item_name} have not been ordered.")

def browse_by_category(stock):
    categories = set(item['category'] for item in stock)
    print(categories, "categories is here ----")
    
    print("Available categories:")
    for category in categories:
        print(category)
    
    category_choice = input("Enter a category to browse: ")
    
    items_in_category = [item for item in stock if item['category'] == category_choice]
    
    if not items_in_category:
        print(f"No items found in the {category_choice} category.")
    else:
        print(f"Items in the {category_choice} category:")
        for item in items_in_category:
            print(f"{item['state']} {item['category']}")


if __name__ == "__main__":
    main()


