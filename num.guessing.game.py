import random
name=random.randint(1, 25)
i=int(input("Enter your guess number between 1 to 25: "))
if i>25:
    print("Your number exceed the limit")
while i != name:
    if i < name:
        print("too low")
    elif i> name:
        print("Too high")
    i = int(input("Try again: "))
print(name,"is the correct number")
print("congartulatin your guess is correct")