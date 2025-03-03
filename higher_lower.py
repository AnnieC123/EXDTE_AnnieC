# Variables
import random
guess_amount = 0
user_guesses = []
loop = ""

# Welcome statement and how to play
print("")
print("Welcome to the higher lower game")
print("I will generate a mystery number between 1-100,")
print("And you have 10 tries to guess the mystery number")
print("")
mystery_number = random.randint(1, 100)


# Game Loop and asking for user guess
while loop == "" and guess_amount < 10:
  print("____________________________________________________")
  print("")
  user_guess = int(input("Enter your guess between 1-100:"))
  print("")
  
# Find out if user_guess is higher or lower than mystery_number
  if user_guess == mystery_number:
    print("Congratulations! You guessed the mystery number!")
    print("")
    break
    
  elif user_guess in user_guesses:
    print("You have already guessed this number.")
    
  elif user_guess > mystery_number and user_guess < 100 and user_guess > 1:
    guess_amount = guess_amount + 1
    user_guesses.append(user_guess)
    print(f"The mystery number is lower than {user_guess}")
    print("")

  elif user_guess < mystery_number and user_guess < 100 and user_guess > 1:
    guess_amount = guess_amount + 1
    user_guesses.append(user_guess)
    print(f"The mystery number is higher than {user_guess}")
    print("")

  else:
    print("Please enter a valid number.")
    print("")


# After game ends:
print(f"The mystery number was {mystery_number}")
print("Game Over.")



