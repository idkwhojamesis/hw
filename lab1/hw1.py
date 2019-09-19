xStr = input("x:")
yStr = input("y:")
zStr = input("z:")

x = int(xStr)
y = int(yStr)
z = int(zStr)

if x>y and x>z:
    print("x")
elif y>z:
    print("y")
else:
    print("z")
