value_in = float(input())
while value_in >= -1.0:
    print(f'Input is {value_in}')
    value_in = float(input())

print('Loop terminated')

############################

input_num = float(input())
while input_num > 1.0:
    input_num /= 8.0
    print(round(input_num, 1))
    
############################

import random
random.seed(5)

keep_bidding = 'y'
next_bid = 0

while keep_bidding == 'y':
   next_bid = next_bid + random.randint(1, 10)
   print(f'I\'ll bid ${next_bid}!')
   print('Continue bidding? (y/n)', end=' ')
   keep_bidding = input()
   
   
############################

"""
Given positive integer num_insects, write a while loop that prints, then doubles, num_insects each iteration. 
Print values ≤ 100. Follow each number with a space.
"""

num_insects = int(input()) # Must be >= 1

while num_insects <= 100:
        print(num_insects, end=" ")
        num_insects *= 2


num_successes = 0

while num_successes < 2:
    curr_intensity = int(input())
    if curr_intensity > 0:
        print(curr_intensity)
        num_successes += 1
        
############################

result = 0
num_in = int(input())

while num_in >= 1:
    if num_in % 4 == 0:
        result += num_in
    else:
        result   -= num_in
    num_in = int(input())

print(f'Result is {result}')

############################

input_num = int(input())

while input_num !=-5 :
    print('Not found -5 yet')
    input_num = int(input())

print('Found -5!')

############################

input_word = input()

while input_word != 'Over':
    item_count= int(input())
    if item_count < 45:
        print(input_word + ': reorder soon')
    input_word = input()
    
############################

previous_val = int(input())
current_val = int(input())
print(f'Sequence starts at {previous_val}.')


while current_val >= previous_val:
    print(str(current_val) + ' is greater than or equal to ' + str(previous_val) + '. Sequence is not decreasing.')
    previous_val = current_val
    current_val = int(input())
    
print(f'{current_val} breaks the sequence.')        
