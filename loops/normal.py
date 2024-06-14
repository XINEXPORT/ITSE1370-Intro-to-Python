num_values = int(input())

values = [float(input()) for _ in range(num_values)]

max_value = max(values)

for value in values:
    normal_value = value / max_value
    print(f'{normal_value:.2f}')
