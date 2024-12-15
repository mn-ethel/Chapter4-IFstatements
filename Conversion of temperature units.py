T=int(input("Enter a temperature:"))
U=input("What unit is the temperature in? (farenheit/celsius):")
if U== "farenheit":
    C=5/9 *(T-32)
    print(T, "farenheit is equal to" ,C, "degrees celsius.")
elif U== "celsius":
    F=9/5 *T+32
    print(T,"degree celsius is equal to",F,"Farenheit.")
else:
    print("Invalid entry please specify whether farenheit or celsius!")


