seconds_max = int(input())

print('Seconds lapsed:', end=' ')

for i in range(0, seconds_max + 1):
    print(i, end=' ')
print()

###########

address_minimum = int(input())
address_maximum = int(input())

print('House numbers:', end=' ')

for i in range(address_minimum, address_maximum):
    print(i, end=' ')
print()

############

first_signal = int(input())
last_signal = int(input())

print('Signals received:', end=' ')

for curr_signal in range(first_signal, last_signal+1):
    if curr_signal % 2 == 0:
        print(curr_signal, end=' ')
print()
