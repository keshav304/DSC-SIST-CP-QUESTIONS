# Bigger is Greater: https://www.hackerrank.com/challenges/bigger-is-greater
from itertools import permutations


def biggerIsGreater(w):
    if len(w) == 1:
        return "no answer"
    if w.count(w[0]) == len(w):
        return "no answer"
    arr = list(permutations(w))
    arr2 = []
    for i in arr:
        arr2.append("".join(i))
    arr2 = list(set(arr2))
    arr2.sort()
    if w == arr2[-1]:
        return "no answer"
    for i in range(len(arr2) - 1):
        if arr2[i] == w:
            return arr2[i + 1]


n = int(input())
arr = [input() for _ in range(n)]
for i in arr:
    print(biggerIsGreater(i))

"""
def permutation(w):
    if w.count(w[0])==len(w):
        return "no answer"
    # length of string
    length = len(w)

    # total strings possible of length "length" with characters of w
    total = math.factorial(length)

    # array to store every possible string
    arr = []
    for i in range(total):
        strr = list(w)
        # update the value of current no after every iteration it main loop remains unaffected
        currentNumber = i
        # temporary string to hold value of each string
        tempString = ""
        for div in range(length, 0, -1):
            q = currentNumber / div
            r = currentNumber % div

            tempString += strr[int(r)]
            strr.pop(int(r))
            currentNumber = q
        arr.append(tempString)
    arr = list(set(arr))
    arr.sort()
    return arr
"""
