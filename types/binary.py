##binary to decimal conversion
binary_string = '10001000'

decimal = int(binary_string, 2)
print(decimal)

#decimal to binary conversion
decimal = int(input())
binary = bin(decimal)[2:]
print(binary)



