import random 
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
images = [rock, paper, scissors]
user_choice = input("What do you Choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. \n")
user_choice = int(user_choice)
print(images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose :")
print(images[computer_choice])

if user_choice == 0 and computer_choice == 2:
  print("You win!")
  
elif user_choice == 0 and computer_choice == 1:
  print("You lost.")

elif user_choice == 0 and computer_choice == 0:
  print("Game draw...")

elif user_choice == 1 and computer_choice == 0:
  print("You win!")

elif user_choice == 1 and computer_choice == 2:
  print("You lost.")

elif user_choice == 1 and computer_choice == 1:
  print("Game draw...")


elif user_choice == 2 and computer_choice == 1:
  print("You win!")

elif user_choice == 2 and computer_choice == 0:
  print("You lost.")

elif user_choice == 2 and computer_choice == 2:
  print("Game draw...")

else:
  print("Wrong input!!!")



