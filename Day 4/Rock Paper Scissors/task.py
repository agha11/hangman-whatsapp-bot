rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# print(scissors)
import random
options = [rock, paper, scissors]
user_choice = int(input("Enter your choice 0 for rock, 1 for paper and 2 for scissors): \n"))
if user_choice >= 0 and user_choice <=2:
    print(options[user_choice])
computer_choice = random.randint(0,2)
print("Computer chose: ")
print(options[computer_choice])
if user_choice >=3 or user_choice < 0:
    print("You enter an invalid option, You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == 2 and computer_choice == 0:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif computer_choice < user_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a tie!")
