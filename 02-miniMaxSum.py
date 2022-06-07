# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers.
# Ex. List = [1, 2, 3, 4, 5]
# Ans. min is 10 (1 + 2 + 3 + 4), max is 14 (2 + 3 + 4 + 5)

def miniMaxSum(arr):
    newArr = []
    n = len(arr)
    sum1, sum2 = 0, 0
    
    for x in range(0, n):
        newArr.append(arr[x])
    
    newArr.sort()
    
    for x in range(0, n-1):
        sum1 += newArr[x]
    for x in range(1, n):
        sum2 += newArr[x]
    
    print(str(sum1) + " " + str(sum2))
