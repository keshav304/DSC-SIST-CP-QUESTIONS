# problem- https://www.hackerrank.com/challenges/permutation-equation/problem
def permutationEquation(p):
    n = len(p)
    arr = []
    for i in range(1, n + 1):
        for j in p:
            if i == p[p[j - 1] - 1]:
                arr.append(j)
    return arr
