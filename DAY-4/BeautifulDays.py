# problem - https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem
# Complete the beautifulDays function below.

def beautifulDays(i, j, k):
    b_days = 0
    for n in range(i,j+1):
        if (max(n,int(str(n)[::-1]))-min(n,int(str(n)[::-1])))%k==0:
            b_days+=1
    return b_days
