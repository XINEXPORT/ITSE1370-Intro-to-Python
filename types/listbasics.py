# Define my_list containing user inputs my_flower1, my_flower2, and my_flower3
my_flower1 = input()
my_flower2 = input()
my_flower3 = input()
my_list = [my_flower1, my_flower2, my_flower3]

# Define your_list containing user inputs your_flower1 and your_flower2
your_flower1 = input()
your_flower2 = input()
your_list = [your_flower1, your_flower2]

# Define our_list by concatenating my_list and your_list
our_list = my_list + your_list
print(our_list)

# Append the user input their_flower to the end of our_list
their_flower = input()
our_list.append(their_flower)
print (our_list)

# Replace my_flower2 in our_list with their_flower
our_list[1] = their_flower
print(our_list)

# Remove the first occurrence of their_flower from our_list without using index()
our_list.remove(their_flower)
print(our_list)

# Remove the second element of our_list
del our_list[1]
print(our_list)



