#input is 25.0 and 3.1599

mileage = float(input())
gas = float(input())

value1 = gas / mileage * 20
value2 = gas / mileage * 75
value3 = gas / mileage * 500

print(f'{value1:.2f} {value2:.2f} {value3:.2f}')
