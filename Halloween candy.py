candy_amount=int(input("Guess the number of candies in the bowl"))
R=candy_amount%5
W=candy_amount%6
T=candy_amount%7
if candy_amount>200:
    print("That is not right!")
if R==2 and W==3 and T==2:
    print("Yaayyy!you won!")
else:
    print("Oops! try again next time")


