# Variables
import random
guess_amount = 0
user_guesses = []
loop = ""
play_again = ""

# Welcome statement and how to play
print("")
print("Welcome to the higher lower game")
print("I will generate a mystery number between 1-100,")
print("And you have 10 tries to guess the mystery number")
print("")
mystery_number = random.randint(1, 100)


# Loops for play again:
while play_again == "":

# Game Loop and asking for user guess
  while loop == "" and guess_amount < 10:
    print("____________________________________________________")
    print("")
    user_guess = int(input("Enter your guess between 1-100:"))
    print("")
    
  # Find out if user_guess is higher or lower than mystery_number
    if user_guess == mystery_number:
      print("Congratulations! You guessed the mystery number!")
      break
      
    elif user_guess in user_guesses:
      print("You have already guessed this number.")
      
    elif user_guess > mystery_number and user_guess <= 100 and user_guess >= 1:
      guess_amount = guess_amount + 1
      user_guesses.append(user_guess)
      print(f"The mystery number is lower than {user_guess}")
      print(f"You have guessed {guess_amount} times.")
      print("")
  
    elif user_guess < mystery_number and user_guess <= 100 and user_guess >= 1:
      guess_amount = guess_amount + 1
      user_guesses.append(user_guess)
      print(f"The mystery number is higher than {user_guess}")
      print(f"You have guessed {guess_amount} times.")
      print("")
      
  
    else:
      print("Please enter a valid number.")
      print("")
  
  
  # After game ends:
  print("Game Over.")
  print(f"The mystery number was {mystery_number}")
  print("")
  
  # Asks user if they want to play again + resets the variables
  print("____________________________________________________")
  print("")
  print("Press 'ENTER' to play again and 'Q' to quit.")
  print("")
  play_again = input("PRESS ENTER TO PLAY AGAIN")
  mystery_number = random.randint(1, 100)
  guess_amount = 0
  user_guesses = []
