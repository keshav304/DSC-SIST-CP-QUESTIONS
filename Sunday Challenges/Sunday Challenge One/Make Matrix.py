# problem https://www.hackerrank.com/contests/dsc-sist-competitive-coding-cookoff/challenges/make-matrix/problem

i,j = map(int, input().split())
arr=[]
arr2=[]
h=0
v=0
n=1
while v<j:
    while h<i:
        arr2.append(n)
        n+=1
        h+=1
    arr.append(arr2)
    arr2=[]
    v+=1
    h=0
for i in arr:
    print(*i)
