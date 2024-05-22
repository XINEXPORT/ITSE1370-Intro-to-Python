#Write a program that reads integers user_num and div_num as input, and outputs user_num divided by div_num three times using floor divisions.

# if the input is
# 2000 2

# the output is 1000 500 250int(input)

def main():
    # Read user input for user_num and div_num
    user_num = int(input())
    div_num = int(input())

    # Perform floor division three times
    result1 = user_num // div_num
    result2 = result1 // div_num
    result3 = result2 // div_num

    # Output the results
    print(result1, result2, result3)

if __name__ == "__main__":
    main()




