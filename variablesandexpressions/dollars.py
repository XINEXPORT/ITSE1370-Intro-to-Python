nickels = float(input())
dimes = float(input())
quarters = float(input())

nickel_value = 0.05
dime_value = 0.10
quarter_value = 0.25

dollars = (nickels * nickel_value) + (dimes * dime_value) + (quarters * quarter_value)

print(f'Amount: ${dollars:.2f}')
