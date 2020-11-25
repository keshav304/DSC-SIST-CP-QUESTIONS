def candies(n, arr):
    total_candies = [1] * n
    # if iTH element in arr is less than i-1TH
    # increase the ith value in total candies by 1 than previous value
    for i in range(1,n):
        if arr[i]>arr[i-1]:
            total_candies[i] = total_candies[i-1] + 1

    #traversing backward in arr
    # if iTH element in arr is more than i-1TH
    # increase the ith value in total candies by 1 than previous value
    for i in range(n-2,-1,-1):
        if arr[i]>arr[i+1]:
            total_candies[i] = max(total_candies[i], total_candies[i+1]+1)



    return sum(total_candies)

n = int(input())
arr = [int(input()) for _ in range(n)]

print(candies(n, arr))
