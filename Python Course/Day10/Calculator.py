"""def add(num1, num2):
  return num1 + num2
  
def mines(num1, num2):
  return num1 - num2
    
def part(num1, num2):
  return num1 * num2
    
def multiply(num1, num2):
  return num1 / num2
    
num1 = int(input("What's the first number ? :"))
num2 = int(input("What's the second number ? :"))
  
  
operations = {"+" : add,
              "-" : mines,
              "*" : part,
              "/" : multiply}
  
for symbol in operations:
  print(symbol)
  
opeartion_symbol = input("Pick an operation symbol from the line above :")
calculation_function =  operations[opeartion_symbol]
answer = calculation_function(num1, num2)
  
print(f"{num1} {opeartion_symbol} {num2} = {answer}") 
decision_1 = input("if you want to Next('y') and No('n') ").lower()

if decision_1 == "y":
  while_control = True
  while while_control is True:
    num3 = int(input("What's the next number ? :"))
    opeartion_symbol = input("Pick an another symbol from the line above :")
    calculation_function =  operations[opeartion_symbol]
    print(f"{calculation_function(answer, num3)}")
    decision = input("if you want to Next('y') and No('n') ").lower()
    if decision == "y":
      while_control = True
    else:
      print("See you next time !")
      while_control = False
else:
  return"""
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

from replit import clear
from art import logo


def add(n1, n2):
  return n1 + n2


def subtract(n1, n2):
  return n1 - n2


def multiply(n1, n2):
  return n1 * n2


def divide(n1, n2):
  return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True

  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(
        f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: "
    ) == 'y':
      num1 = answer
    else:
      should_continue = False
      clear()
      calculator()


calculator()
