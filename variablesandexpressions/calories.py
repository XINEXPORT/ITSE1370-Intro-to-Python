#input is 49 155 148 60
age = float(input())
weight = float(input())
heart_rate = float(input())
time = float(input())

calories = (age * 0.2757 + weight * 0.03295 + heart_rate * 1.0781 - 75.4991) * time / 8.368

print("Calories:", round(calories, 2), "calories")




