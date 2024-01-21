import random

easy_level_healt = 10
hard_level_healt = 5

number = random.randint(1,100)

def easy_level():
  easy_level_healt = 10
  for i in range(0, easy_level_healt):
    guess = int(input("Make a guess :"))
    if guess != number:
      easy_level_healt-=1
      print(f"Wrong! .. kalan hak :{easy_level_healt}")
      if guess > number:
          print("Too High!")

      elif guess < number:
          print ("Too Low!")

      else:
          print("You win!")

      if  hard_level_healt == 0:
        print("You lose!")
        break
          
      
    else:
      easy_level_healt = number
      print("Good job!! You win")
      break
    
def hard_level():
  hard_level_healt = 5
  for j in range(0, hard_level_healt):
    guess = int(input("Make a guess :"))
    if guess != number:
      hard_level_healt-=1
      print(f"Wrong! .. kalan hak :{hard_level_healt}")
      if guess > number:
          print("Too High!")

      elif guess < number:
          print ("Too Low!")

      else:
          print("You win!")

      if  hard_level_healt == 0:
        print("You lose!")
        break

    else:
      hard_level_healt = number
      print("Good job!! You win")
      break


print("Hello! Welcome to Predict game.")
print("I kept a number between 1-100 in my mind, try to know!")
level = input("Choose a difficulty. Type 'Easy' or 'Hard' :")

if level == "Easy":
  print("your level is easy. You have 10 attempts. Good luck!")
  easy_level()

elif level == "Hard":
  print("your level is hard. You have 5 attempts. Good luck!")
  hard_level()
else:
  print("Wrong!! Please be carefull. Type : ('Easy') or ('Hard')")
  


