# James Park
# Sept. 16 2019
# Find two values of a specified SUM.

k = 0;
nList = []
s = 0;

# Get inputs
while True:
    print("value", k, "or 'n' to finish")
    nStr = input()
    # Add to list if numeric
    if nStr.isnumeric():
        n = int(nStr)
        nList.append(n)
        k += 1
    # Get sum and break loop if 'n'
    elif nStr == 'n':
        sStr = input("SUM:")
        s = int(sStr)
        break

# Find pairs in nList of sum s
sumFound = False
for x in range(k):
    n1 = nList[x]
    diff = s - n1
    # Sequential search through nList for diff
    for i in range((x+1),k):
        if nList[i] == diff:
            n2 = nList[i]
            sumFound = True
        if sumFound == True:
            break
    if sumFound == True:
        break

# Print results
if sumFound == True:
    print("I found", n1, "and", n2, "for the sum of", s)
else:
    print("Sorry, there is no such pair of values.")


