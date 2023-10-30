print("Welcome to tech quiz game")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
else:
    print("Great! Lets play the game")

score = 0
    
answer = input("Which company developed the Windows operating system? ")
if answer.lower() == "microsoft":
    print("You got it right!")
    score += 1
else:
    print("Sorry, you got it wrong, the correct answer is Microsoft.")

answer = input("What does 'URL' stand for? ")
if answer.lower() == "uniform resource locator":
    print("You got it right!")
    score += 1
else:
    print("Sorry, you got it wrong, the correct answer is Uniform Resource Locator.")
    
answer = input("What is 'Wi-Fi' short for? ")
if answer.lower() == "wireless fidelity":
    print("You got it right!")
    score += 1
else:
    print("Sorry, you got it wrong, the correct answer is Wireless Fidelity.")
    
answer = input("What does 'CPU' stand for in computer terms? ")
if answer.lower() == "central processing unit":
    print("You got it right!")
    score += 1
else:
    print("Sorry, you got it wrong, the correct answer is Central Processing Unit.")
    print("You got " + str(score) + " questions correct.")
    print("Your score is " + str((score / 4) * 100) + "%.")
    
answer = input("What does 'CPU' stand for in computer terms? ")
if answer.lower() == "central processing unit":
    print("You got it right!")
    score += 1
else:
    print("Sorry, you got it wrong, the correct answer is Central Processing Unit.")
    print("You got " + str(score) + " questions correct.")
    print("Your score is " + str((score / 4) * 100) + "%.")
    
