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
        if choice.isnumeric(): 
            if choice == '1':
                # Prompt for and add an item
                item = input("Enter the item to add: ")
                if item.isalpha():
                    shopping_list.append(item)
                else:
                    print("Invalid item name. Only alphabetical characters are allowed.")
            elif choice == '2':
                # Prompt for and remove an item
                item = input("Enter the item you want to remove: ")
                if item in shopping_list:
                    shopping_list.remove(item)
                else:
                    print("Item not found in the list.")
            elif choice == '3':
                # Display the shopping list
                print("Shopping List:")
                for item in shopping_list:
                    print(item)
            elif choice == '4':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        else:
            print("Invalid choice. Please enter a number.")

if __name__ == "__main__":
    main()