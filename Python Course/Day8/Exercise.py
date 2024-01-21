"""def Berk_yapaymi():
  print("Berk yapay mi?")
  print("Ne YaBayği mi?")
  print("Nasiğğ")
  
Berk_yapaymi()"""
"""def greeting(name):
  print(f"Ola {name}")
  print(f"How are you {name} ?")

greeting("Kaan")"""
"""def greet_with(name, location):
  print(f"Ola {name} !")
  print(f"are you in {location} ? ")

greet_with(location = "İstanbul", name = "Kaan")"""


"""def paint_calc(height, width, cover):
    print(f"You'll need {round((height * width) / cover)} cans of paint")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)"""


def prime_checker(number):
  number_checker = True
  
  for i in range(2,number):
    if number % i == 0:
      number_checker = False
  if  number_checker:
    print("It's a prime number !")
  else :
    print("It's not a prime number !")
  
    
     







n = int(input("Check this number: "))
prime_checker(number=n)
