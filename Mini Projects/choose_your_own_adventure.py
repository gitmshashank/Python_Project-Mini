name = input(" Type your name:   ")
print("Welcome", name, "to this adventure!")

answer = input(
    "You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go ? ").lower()

if answer == "left":
        answer = input ("You have come to a river, you can walk around it or swim accorss? ")

        if answer == "swim":
             print("You swan accross and were eaten by an aligator.")
        elif answer == "walk":
            print("You walked for many miles, ran out of water and you lost the game. ")
        else:
             print("Not a valid option")    

elif answer == "right":

    answer = input(" You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back) ? ")
    if answer == "back":
             print("You go back and lose.")
    elif answer == "cross":
            answer = input("You cross the bridge and met and stranger. Did you talk to them?(yes/no) ")
            if answer == "yes":
                  print("You got it, You WON! ")
            elif answer == "no":
                print("Better luck next time, you lose! ")
            else:
                  print("Not a valid option, you lose!")  
    else:
             print("Not a valid option")    

else:
      print("Not a valid option, You lose! ")
    
print("Thank you for trying", name )
