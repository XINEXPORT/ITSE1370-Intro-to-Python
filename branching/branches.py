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

