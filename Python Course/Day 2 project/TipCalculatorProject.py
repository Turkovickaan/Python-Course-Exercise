print("Welcome to the tip calculator.")

total_bill = float(input(" What was the totel bill? $"))
percentage = int(
  input("What percentage tip would you like to give? 10, 12, or 15? "))
people_number = int(input("How many people to split the bill? "))

if percentage == 12:
  percentage = 1.12
elif percentage == 10:
  percentage = 1.10
elif percentage == 15:
  percentage = 1.15

tip = round((total_bill / people_number) * percentage, 2)
print(f"Each person should pay: ${tip}")
