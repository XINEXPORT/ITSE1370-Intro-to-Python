visited_list_name = input()
place1 = input()
place2 = input()
place3 = input()

places_visited_str = visited_list_name + ': ' + place1 + ', ' + place2 + ', ' + place3  

print(places_visited_str)

#########################

state_code1 = input()
state_code2 = input()
city1 = input()
city2 = input()

state_codes_list = [state_code1, state_code2]
cities_list = [city1, city2]

print(state_codes_list)
print(cities_list)

#########################

months_list = [int(input()), int(input()), int(input()), int(input())]

print(months_list[3] - months_list[1])
