orig_string = input()
sub_string = orig_string[0:4]
print(sub_string)

############

my_string = input()
partial_saying = my_string[3:-3]
print(partial_saying)

############

my_string = input()
partial_string = my_string[:8] + my_string[9:]
print(partial_string)

############

my_string = input()
half = len(my_string)//2
sub_lyric = my_string[half::2]
print(sub_lyric)
