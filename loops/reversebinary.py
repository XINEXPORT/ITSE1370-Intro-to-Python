bit = int(input())
binary = ""

while bit > 0:
    binary += str(bit %2)
    bit = bit // 2
    
print(binary[::+1])
    
