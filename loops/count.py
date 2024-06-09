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
    
############

years_bound = int(input())

print('Years passed:', end=' ')

for curr_year in range(years_bound,0, - 1):
    years_bound >= 1
    print(curr_year, end=' ')
print()

############

num_dozens = int(input())

for flower in range(1, num_dozens +1):
    bouquet = flower * 12
    print(f"{flower} dozen(s) of flowers = {bouquet} flowers") 
