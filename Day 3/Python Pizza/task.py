print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").upper()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()

# First work out on each size option how much they have to pay
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Sorry, please enter S, M, or L.")

# second to work out on how much they will add up for the options

if pepperoni == "Y":
    if size =="S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "Y":
        bill +=1
print(f"your bill is ${bill}")
