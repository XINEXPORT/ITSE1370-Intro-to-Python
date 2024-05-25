#inputs
# 9
# 13
# 10
# 5
# 11

years_list = [int(input()), int(input()), int(input())]
add_list = [int(input()), int(input())]

if 13 in years_list:    
    years_list.remove(13)

if 10 in years_list:
    years_list.remove(10)

years_list.extend(add_list)

print(years_list)
