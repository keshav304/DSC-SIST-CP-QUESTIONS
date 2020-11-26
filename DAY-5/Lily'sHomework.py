# Lily's Homework: https://www.hackerrank.com/challenges/lilys-homework
def lilysHomework(arr):
    l= len(arr)
    print(arr)
    asec = sorted(arr)
    dsec = sorted(arr, reverse=True)
    asec_map = {}
    dsec_map = {}
    asec_sum = 0
    desc_sum =0
    for i in range(l):
        asec_map[asec[i]] = i
    for i in range(l):
        dsec_map[dsec[i]] = i
    for i in range(l):
        if arr[i] != asec[i]:
            asec_map[arr[i]],asec_map[asec[i]] =asec_map[asec[i]],asec_map[arr[i]]
            asec_sum+=1
    print(asec_sum)
    for i in range(l):
        if arr[i] != dsec[i]:
            dsec_map[arr[i]],dsec_map[dsec[i]] =dsec_map[dsec[i]],dsec_map[arr[i]]
            asec_sum+=1
    print(desc_sum)
    return min(asec_sum, desc_sum)



print(lilysHomework([7, 15, 12, 3]))
