# try to fix

def read_hour():
    hour = int(input("Enter hour: "))
    return hour

def read_minute():
    minute = int(input("Enter minute: "))
    return minute

def read_second():
    second = int(input("Enter second: "))
    return second

def to_seconds(hour, minute, second):
    hour   = hour*3600
    minute = minute*60
    return (hour+minute+second)

def time_elapsed(start_time, finish_time):
    time = finish_time - start_time
    he = int(time / 3600)
    me = (time - (he*3600))//60
    se = time - ((he*3600)+(me*60))
    return f"{he} hours {me} minutes {se} seconds."

def read_time():
    print('>> ', end='')
    hour = read_hour()
    print('>> ', end='')
    minute = read_minute()
    print('>> ', end='')
    second = read_second()
    return to_seconds(hour, minute, second)

print('Start time:')
start_time = read_time()
print('Finish time:')
finish_time = read_time()
print('Elapsed time is', time_elapsed(start_time, finish_time))
print(finish_time - start_time)