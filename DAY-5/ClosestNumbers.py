# Closest Numbers: https://www.hackerrank.com/challenges/closest-numbers
# Complete the closestNumbers function below.
def closestNumbers(arr):
    arr.sort()
    result = min([arr[i]-arr[i-1] for i in range(1,len(arr))])
    print(arr)
    print(result)
    summ=[]
    for i in range(1,len(arr)):
        if (arr[i]-arr[i-1])==result:
            summ.append(str(arr[i-1]))
            summ.append(str(arr[i]))
    return summ

n = int(input())

arr = list(map(int, input().rstrip().split()))

print(closestNumbers(arr))
