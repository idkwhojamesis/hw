# James Park
# Sept. 9, 2019
# Code to use int, float, and string

# Get input for name, age, salary (gets strings)
nameStr = input("Name: ")
ageStr = input("Age: ")
salaryStr = input("Salary: ")

# Convert ageStr to int
age = int(ageStr)
if age >= 62:
    print ("You are ready for early retirement!")

# Convert salaryStr to float
salary =  float(salaryStr)
if salary > 90000.00:
    print ("You are making a large amount of money per year.")

# Output
print("Hello,", nameStr)
print("Age is", age)
print("Your salary is", salary)
