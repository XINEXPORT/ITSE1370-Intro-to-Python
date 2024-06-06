num_input = int(input("Enter the number of values: "))
destination_list = []

for i in range(num_input):
    value = input()
    destination_list.append(value)

for value in destination_list:
    print(value, "picked")

######

val_count = int(input())
num_list = []
for i in range(val_count):
    num_list.append(int(input()))

print(f'List has {val_count} elements:')
