# Setting up the main non-changing variables for the game
PLAY_PRICE = 1
UNICORN = 5.00
ZEBRA_HORSE = 0.50
DONKEY = 0.00
MAXIMUM_SPEND = 10
import random

# List of tokens and the changing variables
TOKEN_LIST = ["UNICORN", "ZEBRA", "ZEBRA", "ZEBRA", "HORSE", "HORSE", "HORSE", "DONKEY", "DONKEY"]
input_money = 0
token = "none"
earnt_money = 0
initial_input_money = 0
play_again = "none"

# Messages at the start
print("The cost to play is $1")
print("The maximum that you can spend is $10")
print("The amount of money that you get from each token is as listed below:")
print("-UNICORN = $5.00")
print("-ZEBRA or HORSE = $0.50")
print("-DONKEY = $0.00")
print("")

# Asks user for how much money they want to input / saves it in variables
while input_money == 0:
  input_money = int(input("Enter an integer between $1 and $10 that you would like to spend:"))
  if input_money < 1:
    print("")
    print("Please enter a valid amount")
    print("")
    input_money = 0
  elif input_money > 10:
    print("")
    print("Please enter a valid amount")
    print("")
    input_money = 0
initial_input_money = input_money

# Loop that starts the game / check if user has enough balance
print("")
keep_going = input("PRESS ENTER TO START")
print("________________________________________________________")
print("")
while keep_going == "":
  if keep_going == "" and input_money >= 1:
    input_money = input_money - PLAY_PRICE
    token = random.choice(TOKEN_LIST)
    print(f"You got {token}!")
  
    if token == "UNICORN":
      earnt_money = earnt_money + UNICORN
      print(f"You earnt ${UNICORN}")
    
    elif token == "DONKEY":
      earnt_money = earnt_money + DONKEY
      print(f"You didn't earn any money...") 
      
    elif token == "ZEBRA "or "HORSE":
      earnt_money = earnt_money + ZEBRA_HORSE
      print(f"You earnt ${ZEBRA_HORSE}")
      
      
# ask user if they want to keep playing
    print("")
    print(f"Your total earnt money is ${earnt_money}")
    print(f"You have ${input_money} left to spend.")
    print("")
    print("Would you like to keep going?")
    keep_going = input("Press ENTER to keep going, type 'Q' to stop playing.")
    print("________________________________________________________")
    print("")
    
# If the user does not have enough money:
  elif input_money == 0:
    print("You don't have enough money to spend.")
    keep_going = "q"
    
  
# Calculates total money and profit / Prints out after the game has ended
print("")
print("Game over.")
total_money = earnt_money + input_money
total_profit = total_money - initial_input_money
print(f"Your total balance is ${total_money}")

# Prints out different statements depending on whether your total profit is + or -
if total_profit < 0:
  print(f"Your balance from this game is ${total_profit}. You are in debt.")
else:
  print(f"You have profited a total of ${total_profit}. Good job!")
