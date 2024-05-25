# #inputs
# # 9
# # 13
# # 10
# # 5
# # 11

years_list = [int(input()), int(input()), int(input())]
add_list = [int(input()), int(input())]

if 13 in years_list:    
    years_list.remove(13)

if 10 in years_list:
    years_list.remove(10)

years_list.extend(add_list)

print(years_list)

###########################
"""If the input is:
11
13
9
12
then the output is:
12 is found at index 3 of [11, 13, 9, 12]"""

# Reads two values from input into years_list1
years_list1 = [int(input()), int(input())]
# Reads two values from input into years_list2
years_list2 = [int(input()), int(input())]

years_list3 = years_list1 + years_list2 
index_found = years_list3.index(13)

print(f'12 is found at index {index_found} of {years_list3}')
