from random import randint
Q=randint(1,10)
G=int(input("Enter your guess:"))
if G==Q:
    print("That is correct you got it right!")
else:
    print("Oops! you didn't quite get it")