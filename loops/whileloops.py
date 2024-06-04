value_in = float(input())
while value_in >= -1.0:
    print(f'Input is {value_in}')
    value_in = float(input())

print('Loop terminated')

input_num = float(input())
while input_num > 1.0:
    input_num /= 8.0
    print(round(input_num, 1))

