try:
    arr = [input() for _ in range(int(input()))]
    for i in arr:
        if (len(i) % 2) == 0:
            f = i[:int(len(i) / 2)]
            r = i[int(len(i) / 2):]
            if sorted(f) == sorted(r):
                print("YES")
            else:
                print("NO")
        else:
            mid = int((len(i) - 1) / 2)
            f = i[:mid]
            r = i[mid + 1:]
            if sorted(f) == sorted(r):
                print("YES")
            else:
                print("NO")
except EOFError as e:
    print(end=" ")
