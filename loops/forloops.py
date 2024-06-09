num_input = int(input("Enter the number of values: "))
destination_list = []

for i in range(num_input):
    value = input()
    destination_list.append(value)

for value in destination_list:
    print(value, "picked")

############

val_count = int(input())
num_list = []
for i in range(val_count):
    num_list.append(int(input()))

print(f'List has {val_count} elements:')

############

val_count = int(input())
number_list = []
for i in range(val_count):
    number_list.append(int(input()))

print(f'List has {val_count} elements:')

for num in number_list:
    print('Input =', num)
    
############

in_count = int(input())
member_list = []
for i in range(in_count):
    member_list.append(input())

print(f'List has {in_count} elements:')

for x in reversed(member_list):
    print('(' + x + ')', end = '')

print()

############

student_dict = {
    'Kit': 42,
    'Sid': 75,
    'Eve': 78,
    'Ted': 51,
    'Leo': 88
}

new_name = input()
new_score = int(input())
student_dict[new_name] = new_score

for student, score in student_dict.items():
    print(f"{student}'s exam score:", score)

total_score = sum(student_dict.values())
average_value = total_score / len(student_dict)

print(f'Average exam score: {average_value:.2f}')

