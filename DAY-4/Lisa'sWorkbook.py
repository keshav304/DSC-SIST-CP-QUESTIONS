#probem https://www.hackerrank.com/challenges/lisa-workbook/problem
def workbook(n, k, arr):
    ans = 0
    page = 1
    for i in arr:
        for j in range(1, i + 1):
            # if page no is in range
            if page == j:
                ans += 1
            # new page if all problems covered or maximum problems for the page reached
            if j == i or j % k == 0:
                page += 1
    return ans


nk = input().split()
n = int(nk[0])

k = int(nk[1])

arr = list(map(int, input().rstrip().split()))

print(workbook(n, k, arr))
