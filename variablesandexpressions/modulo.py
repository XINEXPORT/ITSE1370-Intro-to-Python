# """
# Integers total_volume and lamp_volume are read from input. 
# Assign num_lamps with the maximum number of lamps that can fit in a box with volume total_volume cubic units, 
# if each lamp takes up lamp_volume cubic units.
# """

# total_volume = int(input())
# lamp_volume = int(input())

# num_lamps = total_volume // lamp_volume

# print('Maximum number of lamps:', num_lamps)

# """
# Integer user_value is read from input. Assume user_value is greater than 1000 and less than 99999. 
# Assign ones_digit with user_value's ones place value.
# """
# user_value = int(input())

# ones_digit = user_value % 10

# print('Value in ones place:', ones_digit)

"""
Convert total_inches to yards, feet, and inches, finding the maximum number of yards, then feet, then inches.
"""
total_inches = int(input())

num_yards = total_inches // 36
num_feet = (total_inches % 36) // 12
num_inches = total_inches % 12

print('Yards:', num_yards)
print('Feet:', num_feet)
print('Inches:', num_inches)



