nums = [1, 4, 15, 456]

max_even = None
for num in nums:
    if num % 2 == 0: # The number is even?        
        if max_even == None or num > max_even:  # Greatest even number seen?
            max_even = num

print(max_even)

cnt_odd = 28
num = [1, 4, 15, 456]

for i in num:
    if i % 2 == 1:
        cnt_odd += 1
        
print(cnt_odd)
