num_people = int(input())

if (num_people >= 1350) or (num_people <= 4850):
    print('Large town')
else:
    print('Not a large town')
    
###########################

num_residents = int(input())

if (num_residents >= 800) and (num_residents <= 4800):
    print('Mid-size town')
else:
    print( 'Not a mid-size town')
    
 ###########################
# The temperature of titanium in degrees Celsius is read from input into variable degree_val. If degree_val is:

#  1670 degrees Celsius, output 'New state: solid'.
#  1670 degrees Celsius and < 3200 degrees Celsius, output 'New state: liquid'.

degree_val = int(input())

if degree_val <= 1670:
    print('New state: solid')
elif (degree_val > 1670) and (degree_val < 3200):
    print('New state: liquid')
else:
    print('New state: gas')
    
###########################
# If input_year is in the inclusive range:

# 1950 - 1959, output 'The 50s'.
# 1960 - 1969, output 'The 60s'.
# 1970 - 1979, output 'The 70s'.
# Otherwise, output 'Not in the period of research'.

input_year = int(input())

if (input_year >= 1950) and (input_year <= 1959):
    print('The 50s')
elif (input_year >= 1960) and (input_year <= 1969):
    print('The 60s')
elif (input_year >= 1970) and (input_year <= 1979):
    print('The 70s')
else: 
    print('The Future')


 

