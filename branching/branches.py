num_puppies = 6
   
if num_puppies == 4:
   print('a')
else:
   print('d')
   
print('h')

##################
num_apples = 6
   
if num_apples != 4:
   print('c')
else:
   print('d')
   
print('h')

##################
# Write an if-else statement for the following:
# If barcode_check_digit is not equal to 8, execute group_id = 10. Else, execute group_id = barcode_check_digit.

barcode_check_digit = int(input())  # Program will be tested with values: 6, 7, 8, 9.

if barcode_check_digit != 8:
    group_id = 10
else: 
    group_id = barcode_check_digit

print(group_id)

##################
# Write an if-else statement for the following:
# If num_difference is not equal to -15, execute total_difference = -10. Else, execute total_difference = num_difference.

num_difference = int(input())  # Program will be tested with values: -13 -14 -15 -16.

if num_difference != -15:
    total_difference = -10
else:
    total_difference = num_difference

print(total_difference)

##################
# If num_wheels is 12, output 'Twelve-wheel drive'. Otherwise, output 'Not a twelve-wheel drive'.

num_wheels = int(input())

if num_wheels == 12:
    print ('Twelve-wheel drive')
else: 
    print('Not a twelve-wheel drive')
    
    
##################
# If number_of_years is:
# 10, output 'Decade'.
# 100, output 'Century'.
# Otherwise, output 'Other time duration'.

number_of_years = int(input())

if number_of_years == 10:
    print('Decade')
elif number_of_years == 100:
    print('Century')
else: 
    print('Other time duration')
    
    
##################    
# If num_musicians is:
# 3, output 'Trio'.
# 4, output 'Quartet'.
# 5, output 'Quintet'.
# Otherwise, output 'Other number of musicians'.

num_musicians = int(input())

if num_musicians == 3:
    print('Trio')
elif num_musicians == 4:
    print('Quartet')
elif num_musicians == 5:
    print('Quintet')
else: 
    print('Itsa Orchestra, bitch!')
    
##################  
user_grade = int(input())

if user_grade >= 9 and user_grade <= 12:
    print('in high school')
else:
    print('not in high school')
    
#################  
# Complete the if-else statement to output 'Above -20' if the value of input_val is above -20. Otherwise, output '-20 or less'.

input_val = int(input())
   
if input_val > -20:
    print('Above -20') 
else:
    print('-20 or less')

################# 
# Write an if-else statement to output 'Less than a dozen tangerines' if the value of items_bought is less than 12. Otherwise, output 'At least a dozen tangerines'.

items_bought = int(input())

if items_bought < 12:
    print('Less than a dozen tangerines')
else: 
    print('At least a dozen tangerines')

################# 
#Integer bird_count is read from input. If bird_count is greater than 15, then output 'Enough birds'.

bird_count = int(input())

if bird_count > 15:
    print('Enough birds')

################# 
#Integers user_val and new_val are read from input. If user_val is less than or equal to 1000, then assign new_val with 1000.

user_val = int(input())
new_val = int(input())

if user_val <= 1000:
    new_val = 1000

print(f'new_val: {new_val}')

################# 
#Integer num_cars is read from input. If num_cars is less than 9, then output 'An acceptable number of cars'. Otherwise, output 'Too many cars'.

num_cars = int(input())

if num_cars < 9:
    print('An acceptable number of cars')
else: 
    print('Too many cars')
    
################# 
# Integers number_of_items, accepted_groups, and remaining_groups are read from input.
# If number_of_items is less than or equal to 17, then subtract 4 from accepted_groups. Otherwise, add 2 to remaining_groups.

number_of_items = int(input())
accepted_groups = int(input())
remaining_groups = int(input())

if number_of_items <= 17:
    accepted_groups = accepted_groups - 4
else:
    remaining_groups = remaining_groups + 2

print(accepted_groups)
print(remaining_groups)
