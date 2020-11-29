#problem  https://www.hackerrank.com/contests/dsc-sist-competitive-coding-cookoff/challenges/paradoxical-entity

n=int(input())
arr=list(map(int, input().split()))
x=int(input())

element = arr[x-1]
arr.sort()
i = arr.index(element)
print(i+1)
