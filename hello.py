import sys

print("Hello World!")
calculated_number = 8 * 5
print(calculated_number)

float_number = 7.0
print(float_number)

my_string = "My age is "
age_string = my_string + "40 years old"
print("%s and 2 months" % age_string)

print(" %d is my favorite float as a decimal" % float_number)
print("%f is my favorite float" % float_number)

# Try adding a float number to the print statement
# print("Good morning" + float_number)
# error: you can only concatenate str

#Try appending an integer to a string. What happens?
#print("Good morning " + 05)

# PART C
str_len = len(age_string)
print(str_len)

num_inst = age_string.count("years")
print(num_inst)

# 5 We can extract a substring from a string variable using array syntax
sub_string = age_string[2:4]
print(sub_string)
# Extract substring value from character two to four

# 6. We can convert a string from upper to lower case and vice versa using the string.upper()
#    and string.lower() functions
upper_string = age_string.upper()
print(upper_string)
lower_string = age_string.lower()
print(lower_string)

print(age_string[10:12])

# PART D






# in Terminal:  python hello.py "test 1" "test 2"

