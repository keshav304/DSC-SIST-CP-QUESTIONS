t = int(input())
for _ in range(t):
    n, m = input().split()
    n = int(n)
    sum = 0
    for _ in range(n):
        i = input().split()
        if i[0] == 'CONTEST_WON':
            if int(i[1]) <= 20:
                sum = sum + (300 + (20 - int(i[1])))
            else:
                sum += 300
        if i[0] == 'TOP_CONTRIBUTOR':
            sum += 300
        if i[0] == 'BUG_FOUND':
            sum += int(i[1])
        if i[0] == 'CONTEST_HOSTED':
            sum += 50
    print(int(sum / (200 if m == 'INDIAN' else 400)))
