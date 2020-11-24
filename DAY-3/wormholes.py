"""
tle in some cases still working on it
"""

try:
    n, x, y = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    v = list(map(int, input().split()))
    w = list(map(int, input().split()))
    v=set(v)
    w=set(w)
    arr = sorted(arr)
    arr2 = []
    minv= min(v)
    maxw =max(w)
    for i in arr:
        if i[0]<minv or i[1]>maxw:
            arr.remove(i)

    for i in v:
        for j in w:
            for k in arr:
                if i <= k[0] and j >= k[1]:
                    arr2.append(j - i + 1)
    print(min(arr2))

except EOFError as e:
    print(end=" ")