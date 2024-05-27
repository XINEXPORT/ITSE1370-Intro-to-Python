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

###############################

city_info = (input(), input(), int(input()))

city = city_info[0]
state = city_info[1]
zip_code = city_info[2]

print(city)
print(state)
print(zip_code)

###############################

first_name = input()
last_name = input()
state = input()

person_data = (first_name, last_name, state)

print(f'First name: {person_data[0]}, Last name: {person_data[1]}, State: {person_data[2]}')

###############################
from collections import namedtuple

City = namedtuple('City', ['name', 'state', 'population'])

city_name = input()
state_located = input()
population_count = int(input())

city_info = City(city_name, state_located, population_count)

print(f'City name: {city_info.name}, State: {city_info.state}, Population: {city_info.population}')

###############################

"""Person is a named tuple with fields: first_name, last_name, birthday, and age. 
Read three strings and one integer from input. 
Create person_info as a Person tuple, and initialize person_info with first_name, last_name, birthday, and age as the fields."""

from collections import namedtuple

Person = namedtuple('Person', ['first_name', 'last_name', 'birthday', 'age'])

first_name = input()
last_name = input()
birthday = input()
age = input()

person_info = Person(first_name, last_name, birthday, age)

print(f'First name: {person_info.first_name}, Last name: {person_info.last_name}, Birthday: {person_info.birthday}, Age: {person_info.age}')
