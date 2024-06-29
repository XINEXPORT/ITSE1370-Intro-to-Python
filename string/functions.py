# def get_minutes_as_hours(orig_minutes):

#     hours = orig_minutes / 60
#     return hours

# minutes = float(input())
# print(get_minutes_as_hours(minutes))


# def calc_num(parameter):
#     if parameter > 8.0:
#         return 5.1 * parameter
#     else:
#         return parameter + 5.1

# value_read = float(input())

# print(f'{calc_num(value_read):.2f}')


# def compute_result(param1, param2):
#         return(param1 * param2) + 4

# value_read1 = int(input())
# value_read2 = int(input())

# print(compute_result(value_read1, value_read2))

# def print_age_and_name(name, age):
#     print(name + ' is ' + str(age) + ' years old.')

# # Input values
# person_name1 = input()
# person_age1 = int(input())
# person_name2 = input()
# person_age2 = int(input())

# # Output using print_age_and_name function
# print_age_and_name(person_name1, person_age1)
# print_age_and_name(person_name2, person_age2)

# grade = int(input())

# if grade > 6:
#     if grade > 8:
#         category = 'High school'
#     else:
#         category = 'Middle school'
# else:
#     if grade > 0:
#         category = 'Elementary school'
#     else:
#         category = 'Invalid entry'

# print(f'Your category is: {category}')


# plants = input().split()
# colors = input().split()
# separator_char = input()

# print(f'{"Plants".center(21)}|{"Colors".center(21)}')
# print(separator_char * 42)
# print(f'{plants[0].rjust(21)}|{colors[0].rjust(21)}')
# print(f'{plants[1].rjust(21)}|{colors[1].rjust(21)}')
# print(f'{plants[2].rjust(21)}|{colors[2].rjust(21)}')

def mph_and_minutes_to_miles(miles_per_hour, minutes_traveled):
    hours_traveled = minutes_traveled / 60.0
    miles_traveled = hours_traveled * miles_per_hour
    return miles_traveled

miles_per_hour = float(input())
minutes_traveled = float(input())

print(f'Miles: {mph_and_minutes_to_miles(miles_per_hour, minutes_traveled):f}')
