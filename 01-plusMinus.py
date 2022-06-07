# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
# Ex. 5 integers in a list. 3 positive, 1 negative, 1 zero
# Ans: positive = 3/5, negative = 1/5, zero = 1/5

def plusMinus(arr):
    n = len(arr)
    pos, neg, zero = 0, 0, 0
    
    for x in range(0, n):
        if arr[x] >= 1:
            pos += 1
        elif arr[x] == 0:
            zero += 1
        else:
            neg += 1
    
    print(pos / n)
    print(neg / n)
    print(zero / n)
