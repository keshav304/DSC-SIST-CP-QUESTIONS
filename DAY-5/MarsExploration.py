# Mars Exploration: https://www.hackerrank.com/challenges/mars-exploration
def marsExploration(s):
    n = len(s)
    str = "SOS" * (int(n / 3))
    q=0
    for i in range(n):
        if s[i] != str[i]:
            q += 1
    return q


print(marsExploration("SOSSPSSQSSOR"))
