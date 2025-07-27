def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter item name")
            if item:
                shopping_list.append(item)
                print(f"Added '{item}' to the shopping list.")
            else:
                print("Item name cannot be empty.")
            pass
        elif choice == '2':
            # Prompt for and remove an item
            item = input("Enter item name to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"Removed '{item}' from the shopping list.")
            pass
        elif choice == '3':
            # Display the shopping list
            for idex, item in enumerate(shopping_list):
                '''
                print key value pairs in the shopping list
                '''
                print(f"{idex + 1}. {item}")
            if not shopping_list:
                print("Shopping list is empty.")
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()