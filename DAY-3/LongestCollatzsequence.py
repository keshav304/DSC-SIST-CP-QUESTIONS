from typing import Dict


# memoization
def collatz(n, d):
    try:
        return d[n]

    except KeyError:
        if n % 2 == 0:
            d[n] = 1 + collatz(n // 2, d)
        else:
            d[n] = 1 + collatz(3 * n + 1, d)
        return d[n]


def solve(n):
    d = {1: 1}
    for i in range(1, n, 1):
        collatz(i, d)
    v = list(d.values())
    k = list(d.keys())
    ans = k[v.index(max(v))]

    return ans


print(solve(10000000))
