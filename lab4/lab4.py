# James Park
# Oct. 1 2019
# Process airline orders

print("Welcome to Fordham Airlines!")
# Get destination
dest = 0;
while dest != 'c' and dest != 'm' and dest != 'p':
    dest = input("Destination? (c/m/p):")
# Get time
time = -1;
while time < 0 or time > 2400:
    tStr = input("Desired time? (0-2400):")
    time = int(tStr)
# Get weekday/weekend
dayStr = 0;
while dayStr != 'd' and dayStr != 'e':
    dayStr = input("Week(d)ay or week(e)nd?")
if dayStr == 'd':
    day = True
elif dayStr == 'e':
    day = False
else:
    day = False
# Calculate price
mdDay = 150
mdNight = 100
meDay = 180
meNight = 120

if dest == 'm':
    f = 1
elif dest == 'c':
    f = 0.5
elif dest == 'p':
    f = 2

if day == True:
    if time > 500 and time < 1900:
        price = mdDay * f
    elif (time > 1900 or time < 500) and time < 2400:
        price = mdNight * f
elif day == False:
    if time > 500 and time < 1900:
        price = meDay * f
    elif (time > 1900 or time < 500) and time < 2400:
        price = meNight * f
print("price is $", price, sep="")
# Get # of tickets, exit() if <0
ticStr = 'a'
while ticStr.isdigit() == False:
    ticStr = input("# of tickets:")
tic = int(ticStr)
if tic < 0:
    print("Invalid. Exiting")
    exit()
# Print total
total = price * tic
print("Total: $", total, sep="")
# Get payment
payStr = "a"
while payStr.isdigit() == False:
    payStr = input("How much are you paying?")
pay = int(payStr)
if pay < total:
    print("Not enough money! Exiting")
    exit()
# Print change
change = pay - total
print("Change:", change)
print("Your tickets have been ordered.")
