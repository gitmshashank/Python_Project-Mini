import random

top_of_range = input("Type a number  ")

# Check if the input is a valid digit and convert it
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
 
    if top_of_range <= 0:
        print('Please type a number greater than 0 next time! ' )
        quit()
else:
    print('Please type a number next time!.')
    quit()

# Generate random number between 1 and top_of_range
random_number = random.randint(1, top_of_range)
guesses = 0 #Counter for number of guesses

while True :
    user_guess = input("Make a Guess : ")

    # Check if user input is a valid number
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time!.')
        continue

    guesses +=1 # Increment guess count

    if user_guess == random_number:
        print("You got it! It took you {guesses} guesses. ")
        break
    elif user_guess < random_number :
        print ("Too Low!")
    else:
        print("Too High! ")
    
