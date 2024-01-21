import random

stages = [
    '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]

word_list = ["meyhane", "beyran", "parlement", "muşamba", "kiler", "kömürlük"]
hangman_pred = random.choice(word_list)

display = []
for a in hangman_pred:
  display += "_"

print(display)

while_control = 6
print(stages[while_control])
game_control = False
while while_control > 0:
  register_pred = input("Tahmini bir harf giriniz. \n").lower()

  i = 0
  for letter in hangman_pred:
    if register_pred == letter:
      display[i] = letter
      game_control = True
      print(stages[while_control])
    i += 1
  print(display)
  if game_control == False:
    while_control -= 1
  print(f"Kalan Hak : {while_control}")
  game_control = False
  print(stages[while_control])

  if while_control == 0:
    print("Kaybettiniz")
  elif display == list(hangman_pred):
    print("Kazandınız")
    break
  # if "_" not in display:
  # while_control = True
