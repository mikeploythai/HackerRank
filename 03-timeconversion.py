# Given a time in 12-hour AM/PM format, convert it to military (24-hour, hh:mm:ss) time.
# Ex. Convert 12:01:00AM
# Ans. 12:01:00AM = 00:01:00

def timeConversion(s):
    hour = int(s[:2])
    
    if "AM" in s:
        if hour == 12:
            hour = 00
    if "PM" in s:
        if hour != 12:
            hour += 12
    
    return str(hour).zfill(2) + s[2:-2]
