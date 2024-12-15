hour = int(input("Enter hour (1-12): "))
if hour < 1 or hour > 12:
    print("Invalid input. Hour must be between 1 and 12.")
    hour = int(input("Enter hour (1-12): "))

period = int(input("am (1) or pm (2)? "))
if period not in [1, 2]:
    print("Invalid input. Enter 1 for am or 2 for pm.")
    period = int(input("am (1) or pm (2)? "))


hours_ahead = int(input("How many hours ahead? "))

new_hour = (hour + hours_ahead) % 12
if new_hour == 0: 
    new_hour = 12
switches = (hour + hours_ahead) // 12
if switches % 2 == 1:
    period = 3 - period

new_period = "am" if period == 1 else "pm"
print(f"New hour: {new_hour} {new_period}")
