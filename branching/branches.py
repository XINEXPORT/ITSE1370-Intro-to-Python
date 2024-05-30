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





