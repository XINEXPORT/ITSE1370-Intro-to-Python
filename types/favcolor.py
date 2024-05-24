fav_color = "khaki"
least_fav_color = input()

a = f"My favorite color {fav_color} has {len(fav_color)} characters."
b = f"My least favorite color {least_fav_color} has {len(least_fav_color)} characters."

print(a)
print(b)

#######################
fav_fruit = input()
char_index1 = int(input())
char_index2 = int(input())
char1 = fav_fruit[char_index1]
char2 = fav_fruit[char_index2]


print('Fruit chosen:', fav_fruit)
print('Character at index', char_index1, 'is', char1)
print('Character at index', char_index2, 'is', char2)
