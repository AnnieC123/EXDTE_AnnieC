# If Statements and & while Loops
# We can use 'if' statements to execute code if a given condition is met.
# To check if two variables are the same, we use DOUBLE equals (==).
# Python is case sensitive. 'Hello' is not the same as 'hello'.
# We can get around this by using .lower(), .upper(), or .title()
# while loops are useful when we want the program to loop until a given condition is met 
# but we don't know how many times it needs to loop.

# If Statements!
# Create a variable to loop my code
keepgoing = ""
while keepgoing == "":

# Create a variable to store input frp use about their coffee
  like_coffee = input("Do you like coffee? ").lower()

  if like_coffee == "yes":
    print("I like coffee too!")
    
  elif like_coffee == "no":
    print("You are missing out!")
  
  else:
    print("I don't understand!")
  
# Ask user if they want to keep going
  print()
  keepgoing = input("press enter to keep going")
  print()