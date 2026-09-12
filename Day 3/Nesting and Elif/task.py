print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("You can pay $5 to ride the rollercoaster")
    elif age <= 18:
        print("You can pay $7 to ride the rollercoaster")
    elif age <= 24:
        print("You can pay $10 to ride the rollercoaster")
    else:
        print("You can pay $12 to ride the rollercoaster")
else:
    print("Sorry you have to grow taller before you can ride.")
