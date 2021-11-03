# Frank Goshko 11/2/21
# Shopping cart assignment
# 1) Build a Shopping Cart <br>
# Should have the following capabilities
# 1) Takes in input <br>
# 2) Stores user input into a list <br>
# 3) User can add or delete items <br>
# 4) User can see current shopping list <br>
# 5) Loops until user 'quits' <br>
# 6) Upon quiting the program, print out all items in the user's list <br>

from IPython.display import clear_output as co


def show_instructions():
    print("""Type 'add' to add new items to your shopping cart.
Type 'delete' to remove items from your shopping cart.
Type 'quit' to exit the program.
Type 'show' to list all items in your shopping cart.""")
    print("="*50)


def shopping_cart():
    input('Welcome to PyShop! Press any key to continue. ')
    print("="*50)

    items = []
    done = False

    while not done:
        # clear_output()
        co()

        show_instructions()

        choice = input("What is your choice? Add | Delete | Quit | Show ? ").lower()
        if choice == 'add':
            item_new = input("Type in the item you would like to add to your shopping cart. ")
            item_new_amount = input("How many " + item_new + " would you like to add?")

            cart = {
                "item" : item_new,
                "amount" : item_new_amount
            }

            items.append(cart)
        
        elif choice == 'delete':
            for item in items:
                print(str((items.index(item)+1)) + " - " + item["item"])
            item_del = input("Type in the item number you would like to remove from your shopping cart. ")
            x = int(item_del) - 1

            del items[x]

        elif choice == 'show':
            for item in items:
                print(str((items.index(item)+1)) + " - " + item["item"])
            input('Press any key to continue')
        elif choice == 'quit':
            confirm = input('Are you sure you want to quit? Y/N ? ').lower()
            if confirm == 'y':
                done = True
            elif confirm == 'n':
                continue


shopping_cart()
