print("Welcome to my computer quiz!")

score = 0

play = input("Do you want to play? (Y/n): ")

if play != "Y":
    quit()

print("Okay! Lets play!")

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect")
    
answer = input("What does GPU stand for? ").lower()
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What does RAM stand for? ").lower()
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What does PSU stand for? ").lower()
if answer.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%")