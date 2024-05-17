#Write a program that reads integers user_num and div_num as input, and outputs user_num divided by div_num three times using floor divisions.

# if the input is
# 2000 2

# the output is 1000 500 250

user_num = int(input())
div_num = int(input())

for i in range(3):
    divide_input = user_num // div_num
    print (divide_input, end=' ')
    user_num = divide_input




