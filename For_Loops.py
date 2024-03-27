# All types of Loops shown in example
# For Loops
name = 'Srijan'
for i in name:
    print(i)
    if i == "r":
        print("Hey this is special")

colors = ["Violet", "Indigo", "Blue", "Green", "Yellow", "Orange", "Red"]
for colors in colors:
    print(colors)
    for i in colors:
        print(i)

for k in range(5):  # When there is only one data input given it automatically starts from 0
    print(k)

for k in range(5):
    print(k + 1)

for k in range(1, 5):
    print(k)

for k in range(1, 5, 1):
    print(k)

# While loop
i = int(input("Enter any number: "))  # Incremental while loop
while i <= 3:
    i = i + 1
    print(i)
print("Done with the loop")

count = 5
while count > 0:  # Decremental while loop
    print(count)
    count = count - 1

count = 5
while count > 0:
    print(count)
    count = count + 1  # Infinite while loop DO NOT RUN JUST FOR KNOWLEDGE

# Else with while loop
x = 10
while x > 0:
    print(x)
    x = x - 1
else:
    print("Counter is 0")

# Emulating do while loop in python
while True:
    number = int(input("Enter any Positive number: "))
    print(number)
    if not number > 0:
        break
