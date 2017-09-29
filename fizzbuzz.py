
#Naive fizz buzz implementation in python

def divisibleByThree(x):
    return x % 3 == 0

def divisibleByFive(x):
    return x % 5 == 0

print ("Starting Fizz Buzz... ")

for x in range(1, 101):
    if divisibleByThree(x) and divisibleByFive(x):
        print ("Fizz Buzz")
    elif divisibleByFive(x):
        print ("Buzz")
    elif divisibleByThree(x):
        print ("Fizz")
    else:
        print (x)
