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
    
##########################

# Integer lemon_amount is read from input representing the number of lemons. Output 'Unallowable batch' if:

# the number of lemons is fewer than or equal to 15.
# or the number of lemons is 20 or more.
 
lemon_amount = int(input())

if (lemon_amount <= 15) or (lemon_amount >= 20):
    print('Unallowable batch')
    
##########################
# Float temperature_in_celsius is read from input representing a temperature in degrees Celsius. 
# If the temperature is colder than 10.5 degrees Celsius or warmer than 80.5 degrees Celsius, output 'Deny'. Otherwise, output 'Permit'.

temperature_in_celsius = float(input())

if (temperature_in_celsius < 10.5) or (temperature_in_celsius > 80.5):
    print('Deny')
else: 
    print('Permit')
    
##########################
# Integer cherries_count is read from input representing the number of cherries. Output:

# 'Medium case', if there are 60 - 90 cherries inclusive.
# 'Large case', if there are 120 - 150 cherries inclusive.

cherries_count = int(input())

if (cherries_count >= 60) and (cherries_count <= 90):
    print('Medium case')
elif (cherries_count >= 120) and (cherries_count <= 150):
    print('Large case')
else:
    print('Small case')

##########################
# Integer cups_requested is read from input representing the number of cups. Output:

# 'Full carton', if the number of cups is greater than 20 and less than 35.
# 'Jumbo carton', if the number of cups is greater than 75 and less than or equal to 120.
# 'Select another amount', otherwise.

cups_requested = int(input())

if (cups_requested > 20) and (cups_requested < 35):
    print('Full carton')
elif (cups_requested > 75) and (cups_requested <= 120):
    print('Jumbo carton')
else: 
    print('Select another amount')
