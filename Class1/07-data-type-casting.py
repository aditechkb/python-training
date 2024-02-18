#Integer to Float
x = 10
float_x = float(x)
print(float_x)  # Output: 10.0

#Float to Integer
y = 5.7
int_y = int(y)
print(int_y)  # Output: 5

#Integer/Float to String
a = 10
b = 3.14
str_a = str(a)
str_b = str(b)
print(str_a, str_b)  # Output: '10' '3.14'

#String to Integer/Float
num_str = "25"
int_num = int(num_str)
float_num = float(num_str)
print(int_num, float_num)  # Output: 25 25.0

#Boolean to Integer
is_valid = True
int_valid = int(is_valid)
print(int_valid)  # Output: 1

#Integer/Float/String to Boolean
zero = 0
non_zero = 10
empty_string = ""
non_empty_string = "Hello"

bool_zero = bool(zero)
bool_non_zero = bool(non_zero)
bool_empty_string = bool(empty_string)
bool_non_empty_string = bool(non_empty_string)

print(bool_zero, bool_non_zero, bool_empty_string, bool_non_empty_string)  
# Output: False True False True
