simon_sequence = input()
user_sequence = input()
user_score = 0

for i in range(len(simon_sequence)):
    if simon_sequence[i] == user_sequence[i]:
        user_score += 1
    else:
        break

print("User score:", user_score)

####################

applicant_eligibilities = [input(), input(), input(), input()]

for (k, applicant_name) in enumerate(applicant_eligibilities):
    print(f'#{k + 1}: {applicant_name}')

num_athletes = int(input("Enter the number of athletes: "))
athletes_list = [input(f"Enter name for athlete {i+1}: ") for i in range(num_athletes)]

####################

for athlete_index, athlete_name in enumerate(athletes_list):
    print(f'Athlete {athlete_name} is at position {athlete_index + 1}')

####################

num_data = int(input())

list_customers = []
for i in range(num_data):
    list_customers.append(input())

for(idx, customer_name) in enumerate(list_customers):
    if idx % 2 ==0:
        print(customer_name, 'is scheduled for Morning')
    else:
        print(customer_name, 'is scheduled for Afternoon')
