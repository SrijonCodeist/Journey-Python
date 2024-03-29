# Break statements
for m in range(1, 1000, 1):
    print(m, end=" ")
    if m == 999:
        break
    else:
        print("Missisipi")
print("Thank you")

for i in range(12):  # Break Statement
    if i == 10:
        break
    print("5 X", i, "=", 5 * i)

for i in range(12):  # Continue Statement
    if i == 10:
        print("Skip the iteration")
        continue
    print("5 X", i, "=", 5 * i)
