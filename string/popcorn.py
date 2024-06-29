
def print_popcorn_time(bag_ounces):
    if bag_ounces <3:
        print("Too small")
    elif bag_ounces > 10:
        print("Too large")
    else:
        time_seconds = 6 * bag_ounces
        print(f"{time_seconds} seconds")

bag_ounces = int(input())
print_popcorn_time(bag_ounces)
