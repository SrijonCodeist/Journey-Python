# If-else Statements
a = int(input("Enter your age:"))
print("Your age is:", a)
# Conditional Operators Example: >, <, >=, <=, ==, !=
print(a > 18)
print(a < 18)
print(a >= 18)
print(a <= 18)
print(a == 18)
print(a != 18)
if a > 18:
    print("You can drive")
else:
    print("You can not drive")

appleprice = 210
budget = 200
if appleprice <= budget:
    print("Alexa, Add 1kg Apples to the cart.")
else:
    print("Alexa do not add Apples to the cart")

num = int(input("Enter the value of num:"))
if num < 0:
    print("Number is negative")
elif num == 0:
    print("Number is zero")
else:
    print("Number is positive")
print("I am happy now")  # Shows how indentation is important. Prints regardless of if else logic

# Nested if statements
num1 = int(input("Enter the value of num:"))
if num1 < 0:
    print("Number is negative")
elif num1 > 0:
    if num1 <= 10:
        print("Number is between 1-10")
    elif 10 < num1 <= 20:
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is positive")
