my_flower1 = input()
my_flower2 = input()
my_flower3 = input()

your_flower1 = input()
your_flower2 = input()

their_flower = input()

# 1. Define my_list containing my_flower1, my_flower2, and my_flower3
my_list = {my_flower1, my_flower2, my_flower3}

# 2. Define your_list containing your_flower1 and your_flower2
your_list = {your_flower1, your_flower2}

# 3. Define our_list by concatenating my_list and your_list
our_list = my_list | your_list

print(our_list)

# 4. Append their_flower to the end of our_list
our_list.add(their_flower)

print(our_list)

# 5. Replace my_flower2 in our_list with their_flower
our_list = list(our_list)
our_list[our_list.index(my_flower2)] = their_flower
our_list = set(our_list)
print(our_list)


# 6. Remove the first occurrence of their_flower from
# our_list without using index()
our_list.remove(their_flower)
print(our_list)

# 7. Remove the second element of our_list
our_list = list(our_list)
del our_list[1]
our_list = set(our_list)
print(our_list)
