"""Given 4 floating-point numbers. Use a string formatting expression with conversion specifiers to output their product 
and their average as integers (rounded), then as floating-point numbers.

Output each rounded integer using the following:
print(f'{your_value:.0f}')
Output each floating-point value with three digits after the decimal point, which can be achieved as follows:
print(f'{your_value:.3f}')

input is
8.3
10.4
5.0
4.8

output is
2072 7
2071.680 7.125
"""
num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

product = num1 * num2 * num3 * num4
average = (num1 + num2 + num3 + num4) / 4

rounded_product = round(product)
rounded_average = round(average)

float_product = '{:.3f}'.format(product)
float_avg = '{:.3f}'.format(average)

print(f'{rounded_product} {rounded_average}')
print(f'{float_product} {float_avg}')


