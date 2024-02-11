#Arithmetic Operators
a = 10
b = 3

print("Addition:", a + b)       # 13
print("Subtraction:", a - b)    # 7
print("Multiplication:", a * b) # 30
print("Division:", a / b)       # 3.33333 (in Python 3, returns float)
print("Floor Division:", a // b) # 3 (returns integer part)
print("Modulus:", a % b)        # 1 (remainder)
print("Exponentiation:", a ** b) # 1000 (a to the power of b)

#Comparison Operators
x = 5
y = 10

print("Equal to:", x == y)    # False
print("Not equal to:", x != y) # True
print("Greater than:", x > y)  # False
print("Less than:", x < y)     # True
print("Greater than or equal to:", x >= y) # False
print("Less than or equal to:", x <= y)    # True

#Logical Operators
p = True
q = False

print("Logical AND:", p and q) # False
print("Logical OR:", p or q)   # True
print("Logical NOT:", not p)    # False


#Assignment Operators
# Compound assignment
x += 3  # Equivalent to x = x + 3
print("x after addition:", x)  # Output: 8

x *= 2  # Equivalent to x = x * 2
print("x after multiplication:", x)  # Output: 16

x /= 4  # Equivalent to x = x / 4
print("x after division:", x)  # Output: 4.0



#Identity Operators
x = [1, 2, 3]
y = [1, 2, 3]

print("x is y:", x is y)     # False (Different memory locations)
print("x is not y:", x is not y) # True

z = x
print("x is z:", x is z)     # True (Same memory locations)


#Membership Operators
my_list = [1, 2, 3, 4, 5]

print("2 in my_list:", 2 in my_list)       # True
print("6 in my_list:", 6 in my_list)       # False
print("6 not in my_list:", 6 not in my_list)   # True
