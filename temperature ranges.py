temp=float(input("Enter temperature in degrees celsius:"))
if temp<-273.15:
    print("invalid temperature below absolute zero temperature.")
elif temp==-273.15:
    print("Temperature is absolute zero.")
elif -273.15<temp<0:
    print("Temperature is below freezing point.")
elif temp==0:
    print("The temperature is the freezing point.")
elif 0<temp<100:
    print("The temperature is in the normal range.")
elif temp==100:
    print("The temperature is the boiling point.")
else:
    print("The temperature is above the boiling point.")