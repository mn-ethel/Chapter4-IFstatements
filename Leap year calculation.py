year=int(input("Enter the year:"))
A=year%4
B=year%100
C=year%400
if A==0 and B!=0:
    print(year,"is a leap year")
elif  C==0:
    print(year,"is a leap year.")
else:
    print(year,"is not a leap year")