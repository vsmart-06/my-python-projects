import random
choice = ""
comp_choice = ""
result = ""
your_score = 0
comp_score = 0

def valid_single(a):
    while a!="r" and a!="p" and a!="s":
        print("Invalid input.")
        a = input("Enter 'r' for rock, 'p' for paper, 's' for scissors or 'stop' to stop the program: ")
        a = a.lower()
    return a

def valid_more(b):
    while b!="rock" and b!="paper" and b!="scissors" and b!="stop":
        print("Invalid input.")
        b = input("Enter 'r' for rock, 'p' for paper, 's' for scissors or 'stop' to stop the program: ")
        b = b.lower()
    if b=="rock":
        b = "r"
    elif b=="paper":
        b = "p"
    elif b=="scissors":
        b = "s"
    return b

while choice!="stop":
    l = 0
    choice = input("Enter 'r' for rock, 'p' for paper, 's' for scissors or 'stop' to stop the program: ")
    choice = choice.lower()
    for x in choice:
        l+=1
    if l==1:
        choice = valid_single(choice)
    else:
        choice = valid_more(choice)
    if choice!="stop":
        comp_choice = random.choice(["r", "p", "s"])
        if choice=="r" and comp_choice=="s":
            result = "The computer chose scissors, so you won!"
            your_score+=1
        elif choice=="r" and comp_choice=="p":
            result = "The computer chose paper, so you lost."
            comp_score+=1
        elif choice=="p" and comp_choice=="s":
            result = "The computer chose scissors, so you lost."
            comp_score+=1
        elif choice=="p" and comp_choice=="r":
            result = "The computer chose rock, so you won!"
            your_score+=1
        elif choice=="s" and comp_choice=="r":
            result = "The computer chose rock, so you lost."
            comp_score+=1
        elif choice=="s" and comp_choice=="p":
            result = "The computer chose paper, so you won!"
            your_score+=1
        else:
            result = "The computer chose the same symbol as you did so it's a tie."
        print(result)
print("Your final score is:", your_score)
print("The computer's final score is:", comp_score)