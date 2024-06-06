value_in = float(input())
while value_in >= -1.0:
    print(f'Input is {value_in}')
    value_in = float(input())

print('Loop terminated')

input_num = float(input())
while input_num > 1.0:
    input_num /= 8.0
    print(round(input_num, 1))

import random
random.seed(5)

keep_bidding = 'y'
next_bid = 0

while keep_bidding == 'y':
   next_bid = next_bid + random.randint(1, 10)
   print(f'I\'ll bid ${next_bid}!')
   print('Continue bidding? (y/n)', end=' ')
   keep_bidding = input()

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

