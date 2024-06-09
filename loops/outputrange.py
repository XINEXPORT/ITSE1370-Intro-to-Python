first = int(input())
last = int(input())

if  last < first:
    print("Second integer can't be less than the first.")
else:
    print(first, end=" ")

    while first + 5 <= last:
        first += 5
        print(first, end=" ")

    print()
