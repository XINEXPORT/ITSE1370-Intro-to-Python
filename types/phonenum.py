"""Given an integer representing a 10-digit phone number, output the area code, prefix, and line number using the format (800) 555-1212.
input is 8005551212
output is (800) 555-1212
"""

phone_number = int(input())

set_string = str(phone_number)

area_code = set_string[:3]
prefix = set_string[3:6]
line = set_string[6:]

us_format = f"({area_code}) {prefix}-{line}"

print (us_format)
