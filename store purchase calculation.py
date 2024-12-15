H=int(input("How many items are you purchasing?"))
if H<10:
    total_price=H*12
elif 10<=H<=99:
    total_price=H*10
else:
    total_price=H*7
print("The total cost is:",total_price , "$")