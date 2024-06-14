num_rows = int(input())
num_cols = int(input())

for _ in range(num_rows):
    for _ in range(num_cols):
        print('*', end=' ')
    print()

###############

num_rows = int(input())
num_columns = int(input())

for current_row in range (1, num_rows + 1):
    current_column_letter = 'A'
    for current_column in range(1, num_columns + 1):
        print(f'{current_row}{current_column_letter}', end=' ')
        current_column_letter = chr(ord(current_column_letter) + 1)  # Used to increment letters
    print()


###############

first_val = int(input())
second_val = int(input())

count = 0
i = 0
while i < first_val:
    j = 0
    while j < second_val:
        count += 1
        j += 1
    i += 1

print(f'Inner loop ran {count} times')

###############

start_in = int(input())
end_in = int(input())

count = 0
for i in range(start_in):
    for i in range(end_in +1):
        count += 1

print(f'Inner loop ran {count} times')

###############

initial_num = int(input())
final_num = int(input())

for num in range(initial_num, final_num + 1):
    print('*' * num)

################

num_rows = int(input())
num_columns = int(input())

for row in range(num_rows):
    for column in range(num_columns):
        label = chr(65 + row) + str(column + 1)
        print(label, end = ' ')
    print()
