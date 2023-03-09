import random

print("Welcome to GUESS ME")
print("*"*10)
score=0
print("Your score is",score)

while True:
    max=int(input("what maximum guess number would you want : "))
    print("The range is 0 to",max)
    print()

    print("Lets Play")
    print()

    user=input("Enter your guess: ")
    print("You guessed", user)
    print()

    pc=random.randrange(0,max)
    print("I have my number")
    print()

    print("the number is")
    print("*the drumroll*")
    print(pc)
    print()

    if(user==pc):
        print("congrats you guessed it right")
        score+=1
        print("your score is:",score)
        print()
        print("it was luck or you are the all knower")

    else:
        print("uff wrong guess")
        print("your score is:",score)
        print()
        print("keep the morale high")

    x=input("Do you want to continue (Y/N): ")
    if(x=="Y"):
        print("Great, lets play again")
    else:
        print("aww, no problemo")
        False
