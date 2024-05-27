"""A half-life is the amount of time it takes for a substance or entity to fall to half its original value. 
Caffeine has a half-life of about 6 hours in humans. Given caffeine amount (in mg) as input, output the caffeine level after 6, 12, and 24 hours. 
Use a string formatting expression with conversion specifiers to output the caffeine amount as floating-point numbers.
input is 100
output is 
After 6 hours: 50.00 mg
After 12 hours: 25.00 mg
After 24 hours: 6.25 mg

Note: A cup of coffee has about 100 mg. A soda has about 40 mg. 
An "energy" drink (a misnomer) has between 100 mg and 200 mg.
"""

caffeine_mg = float(input())

sixhr = caffeine_mg * (0.5 ** (6/6))
twelvehr = caffeine_mg * (0.5 ** (12/6))
twentyfourhr = caffeine_mg * (0.5 ** (24/6))

print (f"After 6 hours: {sixhr:.2f} mg")
print(f"After 12 hours: {twelvehr:.2f} mg")
print(f"After 24 hours: {twentyfourhr:.2f} mg")
