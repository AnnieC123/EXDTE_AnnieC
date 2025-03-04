# Variables
import random
user_guess = 0
guess_amount = 0
user_guesses = []
loop = ""
play_again = ""
user_rounds = 0
user_score = 0
score_list = []

# Welcome statement and how to play
print("")
print("Welcome to the higher lower game.")
print("I will generate a mystery number between 1-100,")
print("And you have 10 tries to guess the mystery number")
print("You can play up to a maximum of 5 rounds per session.")

# Loops for play again:
while play_again == "":
  while user_rounds == 0:
    print("")
    user_rounds = int(input("How many rounds do you want to play? (1-5):"))
    if user_rounds <= 5 and user_rounds >= 1: 
      print(f"You will play for {user_rounds} round(s).")
      mystery_number = random.randint(1, 100)
      guess_amount = 0
      user_guesses = []
      user_score = 0
      score_list = []
    else:
      print("Please enter a valid number.")
      print("")
      user_rounds = 0
      
    #Loops until the amount of rounds that the user entered is 0:
  while user_rounds >= 0 and user_guess != mystery_number:
    
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
        print(f"The mystery number is LOWER than {user_guess}")
        print(f"You have guessed {guess_amount} time(s).")
        print("")
        
      elif user_guess < mystery_number and user_guess <= 100 and user_guess >= 1:
        guess_amount = guess_amount + 1
        user_guesses.append(user_guess)
        print(f"The mystery number is HIGHER than {user_guess}")
        print(f"You have guessed {guess_amount} time(s).")
        print("")
        
      else:
        print("Please enter a valid number.")
        print("")
        
    # After game ends:
    user_rounds = user_rounds - 1
    print("Game Over.")
    print(f"The mystery number was {mystery_number}.")
    print("")
    
    if user_rounds > 0:
      print(f"You have {user_rounds} rounds left in this game.")
      
    else:
      print("You have no more rounds left.")
      print("____________________________________________________")
      print("")
      break
      
    #Calculate score + add it to the scorelist
    user_score = 10 - (guess_amount)
    score_list.append(user_score)
    user_guess = 0
    user_guesses = []
    guess_amount = 0
    mystery_number = random.randint(1, 100)
    print(f"Your score for this round is {user_score}")
    print("____________________________________________________")
    print("")
      
  # Cacluate best, lowest, and average score (Runs after finished all rounds)
  average_score = round(sum(score_list) / len(score_list))
  best_score = max(score_list)
  worst_score = min(score_list)
  print(f"scorelist: {score_list}")
  print(f"Your BEST score is {best_score}, Good Job!")
  print(f"Your WORST score is {worst_score}")
  print(f"Your AVERAGE score is {average_score}")
  print("____________________________________________________")
  print("")
        
  # Asks User to play again  
  print("Would you like to play again?")
  print("")
  play_again = input("Press 'ENTER' to play again and 'Q' to quit")
  print("")
  print("____________________________________________________")
