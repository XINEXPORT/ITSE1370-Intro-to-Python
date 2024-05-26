# #List colors_list contains four strings read from input. Create a set named unique_colors containing the unique strings in colors_list.
# colors_list = [input(), input(), input(), input()]

# unique_colors = set(colors_list)

# print(sorted(unique_colors))

# ###############################

# animals_remaining = set()

# new_animal1 = input()
# new_animal2 = input()
# new_animal3 = input()
# new_animal4 = input()
# animals_remaining.add(new_animal1)
# animals_remaining.add(new_animal2)
# animals_remaining.add(new_animal3)
# animals_remaining.add(new_animal4)

# remove_animal = animals_remaining.pop()

# num_animals = len(animals_remaining)

# print(f'Number of values remaining: {num_animals}')  

# ###############################

colors_set1 = {'fuchsia'}
colors_set2 = set()
colors_set2.add(input())
colors_set2.add(input())

new_color = input()
colors_set1.add(new_color)

colors_set1.update(colors_set2)

remove_color = colors_set2.pop()

print(f'colors_set1: {sorted(colors_set1)}')
print(f'colors_set2 size: {len(colors_set2)}')
