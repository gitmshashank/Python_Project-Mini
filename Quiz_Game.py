print("Welcome to my Computer Quiz")

playing = input("Do you want to play games? ")

if playing.lower() != "yes":
    quit()
score = 0

print(" Alrighty! Let's Play then :-) ")

answer= input("What does the CPU stands for?  ")
if answer.lower() == "central processing unit":
    print("Correct Answer")
    score +=1
else:
    print("Incorrect!")

answer= input("What does the GPU stands for?  ")
if answer.lower() == "graphics processing unit":
    print("Correct Answer")
    score +=1
else:
    print("Incorrect!")

answer= input("What does the RAM stands for?  ")
if answer.lower() == "randon access memory":
    print("Correct Answer")
    score +=1
else:
    print("Incorrect!")

answer= input("What does the PSU stands for?  ")
if answer.lower() == "power supply unit":
    print("Correct Answer")
    score +=1
else:
    print("Incorrect!")

print("You've got  " + str(score) + "Questions Correct!")
print("You've got  " + str((score / 4) * 100) + "%.yes")
