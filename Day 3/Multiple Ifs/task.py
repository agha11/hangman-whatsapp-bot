print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Ticket Price $5.")
    elif age <= 18:
        bill = 7
        print("Ticket Price $7.")
    elif age <= 24:
        bill = 9
        print("Ticket Price $9.")
    else:
        bill = 12
        print("Ticket price $12.")
    photo = input("Do you want to take the picture? (y/n)?")
    if photo == "y":
        bill += 5
        print(f"your final bill is: ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
