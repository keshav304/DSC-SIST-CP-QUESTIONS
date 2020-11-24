try:
    n= int(input())
    for _ in range(n):
        n = int(input())
        arr = list(map(int, input().split()))
        summ = 1
        for i in range(1,n):
            if arr[i]<arr[i-1]:
                summ=summ+1
            else:
                arr[i] = arr[i-1]
        print(summ)
except EOFError as e:
    print(end=" ")