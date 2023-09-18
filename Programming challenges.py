# Area of a Triangle
base = int(input("Please enter the base value of the triangle: "))
height = int(input("Please enter the height value of the triangle: "))

TriangleArea = base*height/2
print("The area of the triangle is: ",TriangleArea)

# Power Calculator
print("\n")
voltage = int(input("Please enter the voltage: "))
current = int(input("Please enter the current: "))

power = voltage*current
print("The calculated power is: ",power)

# Return the sum of two numbersh
print("\n")
number_1 = int(input("Please enter the first number: "))
number_2 = int(input("Please input the second number: "))
if number_1 % 7 == 0:
    number_1/7
else:
    if number_2 % 7 == 0:
        number_2/7

if number_1 & 11 == 0:
    number_1/11
else:
    if number_2 & 11 == 0:
        number_2/11
    
sumNumbers = number_1 + number_2
print("The sum of the two numbers is: ",sumNumbers)

# Convert Age to Days
age = int(input("Please enter your age: "))
if age <= 0:
    print("Please enter a valid age")
else:
    ageDays = age*365.24
    print("Your age in days is: ",ageDays)
    

