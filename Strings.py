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

# String Slicing
names = "Srijan,lala,Shubham,Harry,Asmita"
print(names[0:6])
print(names[:6])  # automatically puts 0
print(len(names))

Fruits = "Mango"
Len1 = len(Fruits)
print("Apple is a", Len1, "letter word")
print(Fruits[0:5])  # Include 0 but excludes data from 5
print(Fruits[:5])   # automatically puts 0
print(Fruits[1:5])  # Include 1 but excludes data from 5
print(Fruits[0:-3])  # Python automatically puts len(Fruits) in between [0: and -3] like in the code below
print(Fruits[0:len(Fruits)-3])
print(Fruits[-3:-1])
print(Fruits[-4:-2])
