# Frank Goshko 11/2/21
# Module assignment
# Create a Module in Visual Studio Code and Import It
# Module should have the following capabilities:
# 1) Has a function to calculate the square footage of a room
# 2) Has a function to calculate the circumference of a circle
# Program in Jupyter Notebook should take in user input and use imported functions to calculate a circle's circumference or a houses square footage

import mymodule

def geom_calc():
    
    print ("Please select from the following options:")

    done = False

    while not done:

        choice = input("Press 1 for square footage. Press 2 for circumference. Press 3 to quit.")
        if choice == '1':
            length = input("Please enter the length of the room:")
            width = input("Please enter the width of the room:")
            l = int(length)
            w = int(width)
            sf = str(mymodule.square_foot_room(l,w))
            print("The room is " + sf + " square feet.")

        
        elif choice == '2':
            diameter = input("Please enter diameter of the circle:")
            d = float(diameter)
            cir = str(mymodule.circumference(d))
            print("The circle's circumference is " + cir)


        elif choice == '3':
            confirm = input('Are you sure you want to quit? Y/N ? ').lower()
            if confirm == 'y':
                done = True
            elif confirm == 'n':
                continue


geom_calc()

