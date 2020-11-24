try:
    n = int(input())
    for _ in range(n):
        g = int(input())
        for _ in range(g):
            i, n, q = map(int, input().split())
            if i == q:
                print(int(n / 2))
            else:
                print(n - int(n / 2))

except EOFError as e:
    print(end=" ")
# o(1)
"""
brute force TLE o(n^2)
try:
    n = int(input())
    for _ in range(n):
        g = int(input())
        for _ in range(g):
            i, n, q = map(int, input().split())

            if i == q:
                print(int(n / 2))
            else:
                print(n - int(n / 2))
            if i==1:
                arr = [1]*n
            else:
                arr = [2]*n
            for i in range(n):
                for j in range(i+1):
                    if arr[j]==1:
                        arr[j]=2
                    else:
                        arr[j]=1
            if q==1:
                print(arr.count(1))
            else:
                print(arr.count(2))
except EOFError as e:
    print(end=" ")
"""