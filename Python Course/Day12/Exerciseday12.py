"""name = 50

def say_name():
  def says():
    name=52
    print(name)

  says()
print(name)
say_name()"""

enemy = 1


def new_enemy():
  print(f"New enemies : {enemy}")
  return enemy + 1


enemies = new_enemy()
print(enemies)
