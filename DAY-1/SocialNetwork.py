# Problem:- https://codeforces.com/problemset/problem/1234/B1

n,k = map(int, input().split())
karr = list(map(int, input().split()))
arr=[]
for i in karr:
    if len(arr) < k and (i not in arr):
        arr.insert(0, i)
    elif len(arr) == k and (i not in arr):
        arr.pop()
        arr.insert(0, i)
print(len(arr))
print(*arr)
