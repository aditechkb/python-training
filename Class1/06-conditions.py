#if statement
x = 10

if x > 5:
    print("x is greater than 5")


#if-else statement
x = 3

if x % 2 == 0:
    print("x is even")
else:
    print("x is odd")


#if-elif-else statement
x = 85

if x >= 90:
    print("Grade: A")
elif x >= 80:
    print("Grade: B")
elif x >= 70:
    print("Grade: C")
elif x >= 60:
    print("Grade: D")
else:
    print("Grade: F")

#Nested if statements
x = 10

if x > 0:
    if x % 2 == 0:
        print("x is a positive even number")
    else:
        print("x is a positive odd number")
else:
    print("x is not a positive number")


