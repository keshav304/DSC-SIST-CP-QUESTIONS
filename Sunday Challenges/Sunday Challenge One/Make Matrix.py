# Brute force
print(sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0]))

# Better approach
def Sum(n, p):
    return n * (p / n) * ((p / n) + 1) / 2


result = int(Sum(3, 999)) + Sum(5, 999) - Sum(15, 999)
print(int(result))
