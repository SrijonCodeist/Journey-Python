# # PYTHON LISTS
lst1 = [3, 5, 6]
print(lst1)
print(type(lst1))
print(lst1[0])  # Indextation of lists is possible which starts from 0
print(lst1[1])
print(lst1[2])

details = ["Srijan", "Mallik", 9.3, -1.8, 10, True]  # Lists can have all types of data to be stored in it.
print(details)

# # POSITIVE INDEXIING:
detail2 = ["Srijan", "Mallik", "Asmita", "Ghosh", "Ram", "Chandra"]
#            [0]        [1]      [2]       [3]     [4]      [5]
print(detail2[0])
print(detail2[2])
print(detail2[4])

# NEGATIVE INDEXIING:
detail2 = ["Srijan", "Mallik", "Asmita", "Ghosh", "Ramayan", "Chandra"]
#            [-6]      [-5]      [-4]      [-3]       [-2]      [-1]
print(detail2[-2])
print(detail2[-4])
print(detail2[-6])
print(detail2[len(detail2)-6])  # Change the Negative indexing to Positive indexing by using this syntax

# Experiment code
if "Asmita" in detail2:
    print(detail2.index("Asmita"))
else:
    print("No")

# CHECK WHETHER AN ITEM IS PRESENT IN THE LIST
rainbow = ["Violet", "Indigo", "Blue", "Green", "Yellow", "Orange", "Red", ]
if "Blue" in rainbow:
    print("Blue is present")
else:
    print("Blue is absent")

if "lue" in "Blue":  # "in" syntax also works in strings
    print("Yes")
else:
    print("No")

# Range of Index
rainbow1 = ["Violet", "Indigo", "Blue", "Green", "Yellow", "Orange", "Red"]
print(rainbow1)
print(rainbow1[:7])  # Automatically puts Zero index
print(rainbow1[1:])  # Automatically puts len() of the list
print(rainbow1[-1:])   # Automatically puts len() of the list but using NEGATIVE INDEXING
print(rainbow1[:-7])   # # Automatically puts Zero index and since it starts from zero to zero returns none
print(rainbow1[1:7])
print(rainbow1[1:7:2])  # Jump index is when you need to skip some index like in an arithmetic progression
print(rainbow1[::3])  # Automatically puts Zero index and jumps index and returns that data only
print(rainbow1[-7:-1:2])  # Sliced the list from -1 so you want to end before that
