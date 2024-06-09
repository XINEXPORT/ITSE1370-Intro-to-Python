user_input = input()

done = ('done', 'Done', 'd')

while user_input.lower() not in done:
    print(user_input[::-1])
    
    user_input = input()

