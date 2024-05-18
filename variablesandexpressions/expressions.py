""" Computes the total cost of leasing a car given the down payment,
    monthly rate, and number of months """
    
"""Enter down payment: 500
Enter monthly payment: 300
Enter number of months: 60
Total cost: $18500.00"""

down_payment = int(input('Enter down payment: '))
payment_per_month = int(input('Enter monthly payment: '))
num_months = int(input('Enter number of months: '))

total_cost = down_payment + (payment_per_month * num_months)

#another way to write the line above
all_months_cost = payment_per_month * num_months
total_cost = down_payment + all_months_cost

print (f'Total cost: ${total_cost:.2f}')

# The surface area of a sphere is calculated using the formula
# """Ex: If the input is 36.5, then the output is:
# Surface area of a sphere: 16741.53"""

PI = 3.14159
sphere_radius = float(input())
sphere_surface = 4 * PI * (sphere_radius**2)

print(f'Surface area of a sphere: {sphere_surface:.2f}')

#Assign apricots_quantity with the current value of apricots_quantity multiplied by 5.
apricots_quantity = int(input())

print('Initial number of apricots:', apricots_quantity)

apricots_quantity = apricots_quantity * 5

print('Updated number of apricots:', apricots_quantity)

# Assume that dogs weigh 10 pounds each, cobras weigh 12 pounds each, and eagles weigh 14 pounds each. 
# Given variables num_dogs, num_cobras, and num_eagles read from input, 
# compute the total weight of all the dogs, cobras, and eagles, and assign total_weight with the result.

dog_weight = 10
cobra_weight = 12
eagle_weight = 14

num_dogs = int(input())
num_cobras = int(input())
num_eagles = int(input())

total_weight = (num_dogs * dog_weight) + (num_cobras * cobra_weight) + (num_eagles * eagle_weight)

print('Weight:', total_weight)

