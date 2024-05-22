f0 = float(input())

r = 2 ** (1/12)

value1 = f0 
value2 = value1 * r
value3 = value2 * r
value4 = value3 * r

print(f'{value1:.2f} Hz')
print(f'{value2:.2f} Hz')
print(f'{value3:.2f} Hz')
print(f'{value4:.2f} Hz')
