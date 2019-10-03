# James Park
# Oct. 11 2019
# 4-function calculator

# Infinite loop, exit() conditional under inStr
while True:
    # Get inputs, split
    inputs = ["", "", ""]
    while inputs[0].lstrip('-').isdigit() == False or inputs[2].lstrip('-').isdigit() == False or (inputs[1] != '+' and inputs[1] != '-' and inputs[1] != 'x' and inputs[1] != '/'):
        inStr = input("Enter an equation or 0 x 0 to exit:")
        if inStr == "0 x 0":
            exit()
        inputs = inStr.split(" ")

    # Calculate
    a = int(inputs[0])
    b = int(inputs[2])
    if inputs[1] == '+':
        c = a + b
    if inputs[1] == '-':
        c = a - b
    if inputs[1] == 'x':
        c = a * b
    if inputs[1] == '/':
        if b == 0:
            print("Error -- cannot divide by zero")
            continue
        c = a / b

    # Print
    print(inStr, "=", c)
            
