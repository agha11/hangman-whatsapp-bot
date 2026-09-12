friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
import random
random_integer = random.randint(0, 4)
if random_integer == 0:
    print("Alice")
elif random_integer == 2:
    print("Bob")
elif random_integer == 3:
    print("Charlie")
elif random_integer == 4:
    print("David")
else:
    print("Emanuel")

rand_friends = random.randint(1,5)
print(friends[rand_friends])

random.choice(friends)
print(random.choice(friends))