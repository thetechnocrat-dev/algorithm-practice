import math

def largest_n(funct):
    second = 1 * 1000
    minute = second * 60
    hour = minute * 60
    day = hour * 24
    month = day * 30
    year = day * 365
    century = year * 100

    times = {
    'second': second,
    }

    result = []
    for time_unit in times:
        result.append(largest_n_helper(funct, times[time_unit]))

    print result

def largest_n_helper(funct, time):
    run_time = 0
    n = 0
    print time
    while run_time < time:
        n += 100
        run_time = funct(n)
    return n

def lg_n(n):
    return math.log10(n)

def sqrt_n(n):
    return math.sqrt(n)

print largest_n(lg_n)
