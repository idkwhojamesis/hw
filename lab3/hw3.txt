# James Park
# Sept. 22 2019
# Majority-rules circuit

# Three input ints and one output int (using garbage value)
a = [2,2,2]
out = 0;

# Get input
while (a[0]*a[1]*a[2]) != 1 and (a[0]*a[1]*a[2]) != 0:
    str1 = input("Input 1 (True/False):")
    str2 = input("Input 2 (True/False):")
    str3 = input("Input 3 (True/False):")
    
    # Using int so my conditional works
    if str1.isnumeric() and str2.isnumeric() and str3.isnumeric():
        a[0] = int(str1)
        a[1] = int(str2)
        a[2] = int(str3)

# Determine out
count = 0;
for i in range(3):
    if a[i] == 1:
        count += 1
if count >= 2:
    out = 1

# Print
for i in range(3):
    print("Input ", (i + 1), "is", a[i])

print("Output is", out)  
