orig_string = input()
sub_string = orig_string[0:4]
print(sub_string)

############

my_string = input()
partial_saying = my_string[3:-3]
print(partial_saying)

############

my_string = input()
partial_string = my_string[:8] + my_string[9:]
print(partial_string)

############

my_string = input()
half = len(my_string)//2
sub_lyric = my_string[half::2]
print(sub_lyric)


address = 'www.yahoo.com'

separator = '/'
address_tokens = address.split('.')
print(separator.join(address_tokens))

item_name = input()

print(f'{item_name:*^13}')
print(f'{item_name:*<13}')

############


def print_points(name, age, total_points):
    print(f'{name} is {age}')
    print(f'{name} made {total_points} points')

user_name = 'Ron'
user_age = 23
regular_time_points = 24
overtime_points = 6

print_points(user_name, user_age, regular_time_points + overtime_points)

def show(a, b=1, c=4):
    print(f'{c}/{a}/{b}')

show(c=8, a=5)
show(b=2, a=7)


