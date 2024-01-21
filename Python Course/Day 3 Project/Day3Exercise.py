"""print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm? "))

if height >= 120 :
  print("You can ride the rollercoaster! ")
  age = int(input("What is your age? "))
  bill = 0
  if age <12 :
    bill = 5
    print("Please pay 5$ ")
  elif age <= 18:
    bill = 7
    print("Please pay 7$")
  elif age >= 45 & age <= 55:
    print("Everything is going to be ok. Have a ride on us!")
  else:
    bill = 12
    print("Please pay 12$")

  wants_photo = input("Do you want a photo taken? Y or N ")
  if wants_photo == "Y":
    bill += 3

  print(f"Your final bill ${bill}")
else:
  print("Sorry, You have to grow taller before you can ride")"""









"""bmi = round(weight / height**2)

if bmi <= 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi <= 25 : 
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi <= 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi <= 35:
    print(f"Your BMI is {bmi}, you are obese.")
else: 
    print("Your BMI is {bmi}, you are clinically obese.")


else:
  print("Sorry, you have yo grow taller before you can ride.")"""








"""number = int(input("Which number do you want to check? "))

if number % 2 == 0 :
  print("This is an odd number.")
else:
  print("This is an even number.")"""





"""print("Welcome to Python Pizza Deliveries!")
Small_Pizza = 15

Medium_Pizza = 20

Large_Pizza = 25

bill = 0

size = input("What size pizza do you want? S, M, or L ")
if size == "S":
  bill = 15
  
elif size == "M":
  bill = 20
  
else:
  bill = 25


add_pepperoni = input("Do you want pepperoni? Y or N ")
if add_pepperoni == "Y":
  if bill == Small_Pizza:
    bill += 2
  else :
    bill += 3

else:
  bill = bill

  

extra_cheese = input("Do you want extra cheese? Y or N ")
if extra_cheese == "Y":
  bill += 1
else:
  bill = bill
  
  
print(f"Your final bill is: ${bill} ")"""






"""name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combine_string = name1 + name2

t = combine_string.lower()

t_counts = t.count("t") 
r_counts = t.count("r")
u_counts = t.count("u")
e_counts = t.count("e")

true_total = t_counts + r_counts + u_counts + e_counts

l_counts = t.count("l") 
o_counts = t.count("o")
v_counts = t.count("v")
e_counts = t.count("e")

love_total = l_counts + o_counts + v_counts + e_counts

total_score = int(str(true_total) + str(love_total))

if total_score <10 or total_score >90:
  print(f"Your score is {total_score} , you go together like coke and mentos.")

elif total_score >=40 and total_score <= 50:
  print(f"Your score is {total_score}, you are alright together.")

else:
  print(f"Your score is {total_score}")"""




  
