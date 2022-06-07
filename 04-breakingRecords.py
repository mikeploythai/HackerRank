# Given a list, track how many times you change a minimum and maximum number
# Ex. List = [12, 24, 10, 24]
# Ans. min equals 12, then 10. countMin is 1; max equals 12, then 24. countMax is 1.

def breakingRecords(scores):
    min, max = scores[0], scores[0]
    countMin, countMax = 0, 0
    
    for x in scores:
        if x > min:
            min = x
            countMin += 1
        elif x < max:
            max = x
            countMax += 1
    
    return [countMin, countMax]
