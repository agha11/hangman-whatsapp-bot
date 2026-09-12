# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))


import string
import secrets
# 1. Gather input
total_len = int(input("Enter the length of the password characters: (max=14)\n"))
if total_len > 14 or total_len < 1:
    print("Incorrect password length. Program will exit, Please try again.")
    exit()

min_low = int(input("minimum characters of lower alphabet: \n"))
min_upper = int(input("minimum characters of upper alphabet: \n"))
min_digits = int(input("minimum number of digits: \n"))
min_symbols = int(input("minimum number of symbols: \n"))



sum_total = min_low + min_upper + min_digits + min_symbols
if total_len > 14:
    print("Incorrect Password Length, max length is 14 characters")
elif sum_total > total_len:
    print(f"Error: You requested {sum_total} minimum characters, which exceeds your target length of {total_len}!")
else:
    # 2. character pool
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    all_chars = lower + upper + digits + symbols

    password = []
    # 3. add guaranteed characters as input by user
    for char in range(min_low):
        password.append(secrets.choice(lower))
    for char in range(min_upper):
        password.append(secrets.choice(upper))
    for char in range(min_digits):
        password.append(secrets.choice(digits))
    for char in range(min_symbols):
        password.append(secrets.choice(symbols))

    # 4. Fill remaining spots if needed

    remaining_len = total_len - len(password)
    for char in range(remaining_len):
        password.append(secrets.choice(all_chars))

    # 5. Shuffle securely and print

    secrets.SystemRandom().shuffle(password)
    final_password = "".join(password)

    print(f"\nYour generated password ({len(final_password)} char): {final_password}")
