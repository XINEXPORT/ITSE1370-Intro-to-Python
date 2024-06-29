def print_region_capital(capital_name, region_name):
    print(f"{capital_name} is {region_name}'s capital.")

capital1 = input()
region1 = input()
capital2 = input()
region2 = input()

print_region_capital(capital1, capital2)
print_region_capital(region1, region2)


def get_user_num():
    print("FIXME: Finish get_user_num()")
    return -1
def compute_avg(num1, num2):
    print("FIXME: Finish compute_avg()")
    return -1

user_num1 = 0
user_num2 = 0
avg_result = 0

user_num1 = get_user_num()
user_num2 = get_user_num()
avg_result = compute_avg(user_num1, user_num2)

print(f'Avg: {avg_result}')
