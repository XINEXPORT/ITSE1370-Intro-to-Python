def get_minutes_as_hours(orig_minutes):

    hours = orig_minutes / 60
    return hours

minutes = float(input())
print(get_minutes_as_hours(minutes))


def calc_num(parameter):
    if parameter > 8.0:
        return 5.1 * parameter
    else:
        return parameter + 5.1

value_read = float(input())

print(f'{calc_num(value_read):.2f}')


def compute_result(param1, param2):
        return(param1 * param2) + 4

value_read1 = int(input())
value_read2 = int(input())

print(compute_result(value_read1, value_read2))
