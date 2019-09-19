# James Park
# Sept. 26 2019
# Print a bookstore receipt.

# Store book prices as floats
cerv = 41.25
homer = 15.85
shake = 30.50

# Declaring beforehand for isnumeric() check
cStr = "";
hStr = "";
sStr = "";

print("Welcome to the LC Bookstore!")

name = input("Enter your first name: ")

# Get inputs, proceed when appropriate
while cStr.isnumeric() == False or hStr.isnumeric() == False or sStr.isnumeric() == False:
    cStr = input("  # of Cervantes books: ")
    hStr = input("      # of Homer books: ")
    sStr = input("# of Shakespeare books: ")

# Convert
c = int(cStr)
h = int(hStr)
s = int(sStr)

# Calculate prices
pretax = (cerv * c) + (homer * h) + (shake * s)
tax = round(pretax * 0.10, 2)
total = pretax + tax

# Print total, get pay
print("Total cost of order is: $", total, sep="")
payStr = input("How much money will you pay? ")
pay = float(payStr)

# Print receipt
print("----------")
print("Customer:", name)
print("----------")
print("Item          Number   Price")
print("Cervantes     ", c, "         $", (cerv * c), sep="")
print("Homer         ", h, "         $", (homer * h), sep="")
print("Shakespeare   ", s, "         $", (shake * s), sep="")
print("-----")
print("Tax                     $", tax, sep="")
print("-----")
print("Total                   $", total, sep="")
print("User pay                $", pay, sep="")
print("-----")
print("Change                  $", round(pay-total, 2), sep="")
