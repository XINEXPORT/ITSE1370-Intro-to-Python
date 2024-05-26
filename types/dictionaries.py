student_name1 = input()
test_score1 = int(input())
student_name2 = input()
test_score2 = int(input())
student_name3 = input()
test_score3 = int(input())
student_name4 = input()
test_score4 = int(input())

scores_dict = {
student_name1: test_score1,
student_name2: test_score2,
student_name3: test_score3,
student_name4: test_score4,
}

print(f'{student_name1}: {scores_dict[student_name1]}')
print(f'{student_name2}: {scores_dict[student_name2]}')
print(f'{student_name3}: {scores_dict[student_name3]}')
print(f'{student_name4}: {scores_dict[student_name4]}')

#########################

name_age_pairs = {'Jen': 75, 'Sue': 48}

del name_age_pairs ['Jen']

print('Remaining pairs:')
print(name_age_pairs)

num_items = 5
item_weight = 0.5

total = item_weight * num_items

print(total)
