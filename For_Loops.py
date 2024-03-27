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
