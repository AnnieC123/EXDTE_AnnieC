# If we type in text where a number is expected, our program
# crashes and we get a 'ValueError'
# We can prevent the program from crashing by using try / except code
# If we want the question to be asked until a valid response is entered, 
# we need to wrap our 'try / except' code in a 'while' loop”

# Ask user for number
# Loop question sos tht it repeats until a valid number is entered
# Make code recyclable

valid = False
while not valid:
    error = "Whoops! Please enter an integer between 1 and 10"

    try:
        response = int(input("Enter an integer between 1 and 10: "))

        if 1 <= response <= 10:
            valid = True
        else:
            print(error)
            print()

    except ValueError:
        print(error)

print(response)