from replit import clear


print("Welcome to the secret auction program.")
bid_dictionary = []
    


def Secret_Auction():
  name = input("What is your name? : ")
  bid = input("What's your Bid? : $")
  bid_dictionary.append({"name" : name, "bid" : bid})

  ask = input("Are there any other bidders? Type 'yes' or 'no'").lower()
  
  if ask == 'yes':
    clear()
    Secret_Auction()
  else :
    the_winner()
    
def the_winner():
  winner = max(bid_dictionary, key=lambda x:x['bid'])
  print(f"Winner is {winner}")
  
Secret_Auction()

  
  


