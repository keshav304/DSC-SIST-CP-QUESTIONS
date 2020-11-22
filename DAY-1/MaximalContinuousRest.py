# https://codeforces.com/problemset/problem/1141/B?csrf_token=e90f1e683f715b37f554b765f3e6295f

n = int(input())
arr = list(map(int, input().split()))

if arr.count(1) == 0:
    print("0")
elif arr.count(1) == 1:
    print("1")
elif arr.count(1) == n:
    print(n)
else:
    summ = 0
    arr3 = []
    arr2 = arr[:n - 1]
    arr.extend(arr2)
    for i in range(len(arr) - 1):
        if arr[i] == 1 and arr[i + 1] == 1:
            summ = summ + 1
        else:
            arr3.append(summ)
            summ = 0
    print(max(arr3) + 1)
