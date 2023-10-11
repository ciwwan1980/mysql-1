
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
        elif choice == "2":
            search_and_order_item(stock, today, username)
        elif choice == "3":
            browse_by_category(stock, username)
        elif choice == "4":
            print(f"Thank you for your visit, {username}.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

def list_items_in_stock(stock):
    print(stock, "stock is here----")
    
    items_in_warehouse1 = 0
    items_in_warehouse2 = 0 

    for item in stock:
        if item.get('warehouse') == 1:
            items_in_warehouse1 += 1
        elif item.get('warehouse') == 2:
            items_in_warehouse2 += 1
    
    print("Items in stock:\n")
    for item in stock:
        print (f"{item['state']} {item['category']}  {item['date_of_stock']}")
            
    print(f"Total items in warehouse 1: {items_in_warehouse1}")
    print(f"Total items in warehouse 2: {items_in_warehouse2}")


def search_and_order_item():
    print("search_and_order_item")
def browse_by_category():
    print("browse_by_category")

if __name__ == "__main__":
    main()


