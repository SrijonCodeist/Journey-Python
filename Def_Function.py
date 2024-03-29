# Python Functions: Making new functions to minimize code
a = 9
b = 8
gmean = (a * b) / (a + b)  # This code has to be repeated every time I want to calculate Mean
print(gmean)

c = 14
d = 12
gmean2 = (c * d) / (c + d)  # Like this for different input
print(gmean2)


#  So to minimize it we use def function to create user-defined new functions
def calculategmean(variable1, variable2):
    mean = (variable1 * variable2) / (variable1 + variable2)
    print(mean)


def isgreater(variable1, variable2):
    if variable1 > variable2:
        print("First number is greater")
    else:
        print("Second number is greater")


a = 9
b = 8
calculategmean(a, b)
isgreater(a, b)

c = 14
d = 12
calculategmean(c, d)
isgreater(c, d)

e = 8
f = 7
calculategmean(e, f)
isgreater(e, f)
