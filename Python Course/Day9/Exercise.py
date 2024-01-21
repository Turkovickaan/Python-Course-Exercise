"""dictionary = {"bug" : "An error in a program",
              "Function" : "A piece of code that you can",}

print(dictionary["bug"])

dictionary["Loop"] = "The action of doing something"
print(dictionary)

for thing in dictionary:
  print(thing)
  print(dictionary[thing])"""



"""student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for student in student_scores:
  score = student_scores[student]
  if score > 90 :
    student_grades[student] = "Outstanding"
  elif score > 80:
    student_grades[student] = "Exceeds Expectations"
  elif score > 70:
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Fail"
 


print(student_grades)"""


"""cities_visited = ["Paris" ,"Lyon"]

travel_log = [
  {
  "country": "france",
  "cities_visited": ["Paris" ,"Lyon"] ,
  "total_visits" : 12
  },
  
  {
  "country" : "Turkey",
  "cities_visited": ["İstanbul" ,"Ankara"] ,
  "total_visits" : 1222
  }
]

print(travel_log[0])"""





"""travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]


def add_new_country(country, visits, cities):
  print(f"You've visited {country} {visits} times.")
  print(f"You've been to {cities}.")
  
  travel_log.append
  ({
  "country" : country, 
  "visits " : visits, 
  "cities" : cities
  })  
  
add_new_country("Russia", "2", ["Moscow", "Saint petersburg"])"""