import random

def game():
    print("Welcome to rock ,paper and scissor game")
    print()
    print("Enter 1 if you want to play and enter 0 in the choice if you want to quit")
    print()
    n=int(input("Enter:"))
    if n==1:
        print("Let's start the game")
    while True:
        user_choice=input("Enter your choice (rock/paper/scissor):")
        computer=random.choice(["rock","paper","scissor"])
        print()
        print("You're choice",user_choice)
        print()
        print("Computer's choice",computer)
        if user_choice==computer:
            print("Tie")
            continue
        elif user_choice=="rock" and computer=="scissor":
            print("You win")
            continue
        elif user_choice=="scissor" and computer=="paper":
            print("You win")
            continue
        elif user_choice=="paper" and computer=="rock":
            print("You win")
            continue
        elif user_choice=="0":
            break
        else:
            print("You lose")
    print()
    print("Thanks for playing")

game()


