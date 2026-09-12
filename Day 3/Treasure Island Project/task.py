print(r'''
    ;_(/  \)_; 
     ,'\__/',
       (..)
        \/
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("write left or right side of the treasure.")
choice1 = input('You\'re at a crossroad, where you want to go "left" or "right"')

if choice1 == "left" or choice1 == "Left":
    choice2 = input('You\'ve come to a lake, do you want to "swim" '
                    'or want to wait for a "boat."')
    if choice2 == "boat" or choice2 == "Boat":
        choice3 = input("You've arrived at the lake, there are 3 door, red, blue, yellow.Which one you choose.")
        if choice3 == "yellow" or choice3 == "Yellow":
            print("You fell into the hole full of Snakes Game Over.")
        elif choice3 == "red" or choice3 == "Red":
            print("You entered room full of fire. Game Over.")
        elif choice3 == "blue" or choice3 == "Blue":
            print("You find the treasure!")
        else:
            print("Sorry, you choose the wrong door, game over")
    else:
        print("Sorry, you have been attached by angry trout.")
else:
    print("Sorry, you have been attacked by a Grizzly Bear")