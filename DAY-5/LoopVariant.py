# Correctness and Loop Variant: https://www.hackerrank.com/challenges/correctness-invariant
def insertion_sort(l):
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):
           l[j+1] = l[j]
           j -= 1
        l[j+1] = key
