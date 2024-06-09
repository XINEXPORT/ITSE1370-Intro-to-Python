year = 1792
current_year = 2024

while year <= current_year:
    print(year)
    year = year + 4
    
############

target = int(input())
n = int(input())
step = 4
while n <= target:
    print(n * 2)
    n += step

############

num_fruit = int(input())
num_count = 26

while num_count >= num_fruit:
    print('Apple')
    num_count  = num_count - 4

############

user_num = int(input())
x = 25

while x >= user_num:
    print(':')
    x -= 7
