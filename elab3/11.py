# def caltime(s):
#     return s // 3600, s // 60, s % 60

# s = int(input("s: "))
# print(f"{s} seconds equals {caltime(s)[0]} hour(s) {caltime(s)[1]} minute(s) and {caltime(s)[2]} second(s)")

import math

def caltime(s):
    hour   = s // 3600
    if hour < 1:
        minut  = s // 60
    else:
        minut = abs((hour*60) - (s // 60))
    second = s % 60
    return hour, minut, second

s = int(input("s: "))
print(f"{s} seconds equals {caltime(s)[0]} hour(s) {caltime(s)[1]} minute(s) and {caltime(s)[2]} second(s)")

# print(f"{s} seconds equals {caltime(s)[0]} hour(s) {caltime(s)[1]} minute(s) and {caltime(s)[2]} second(s)")
# print("20456 seconds equals 5 hour(s) 40 minute(s) and 56 second(s)")