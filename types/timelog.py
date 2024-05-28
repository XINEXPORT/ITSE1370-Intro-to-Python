day1_hours = int(input())
day2_hours = int(input())

time_log = {'Sunday': day1_hours,
            'Monday': day2_hours
            }

print(f"Sunday: {time_log['Sunday']}")
print(f"Monday: {time_log['Monday']}")

#########

auth_code = int(input())

contact_dict = {765472: 'Tia@milkshakes.org', 
                271913: 'Val@mushrooms.com', 
                546542: 'Gil@cookies.org'}

if auth_code in contact_dict:
    email_address = contact_dict.pop(auth_code)
    print(email_address)

print('Remaining pairs:')
print(contact_dict)
