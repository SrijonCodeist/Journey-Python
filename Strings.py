# Strings
name = "Srijan Mallik"
friend = "Harry"
anotherfriend = "Sukuna"
aloo = '''he said,
i am good.
How are you?
I said "I am good and I want to eat an apple".'''  # ' ' ' triple quotes are used to store multiline strings
print("hello, " + name)
print(str(name) + str(friend) + str(anotherfriend))
print(aloo)
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print("lets use for loop \n")
for character in aloo:
    print(character)
