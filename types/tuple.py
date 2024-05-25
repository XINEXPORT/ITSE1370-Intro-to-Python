from collections import namedtuple

Color = namedtuple('Color', ['name', 'R', 'G', 'B'])

color_data = Color(input(), int(input()), int(input()), int(input()))

name = input("Enter name: ")
R = int(input('R: '))
G = int(input('G: '))
B = int(input('B: '))

data =  Color(name,R,G,B)

print("Name of color: ", name)
print ("R:", color_data.R)
print ("G:", color_data.B)
print ("B:", color_data.G)
