a = int(input())
b = int(input())
c = int(input())

mult = 0
while a < 10:
    mult = b * a
    if mult > c:
        break
    a = a + 1
z = a

print(z)

############

x = int(input())
y = int(input())
z = int(input())

while x < y:
    if x == z:
        print('x == z')
        break
    x += 1 
else:
    print('x == y')
    
############

my_list = ['Greek', 'Nordic', 'Mayan']

for (index, value) in enumerate(my_list):
    print(index, value)
