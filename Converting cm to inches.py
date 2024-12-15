L=int(input("Enter length in centimeters:"))
if L<0:
    print("Invalid entry!")
else:
    I=L/2.54
    print("The value of ",L, "centimeters iin inches is",I)
