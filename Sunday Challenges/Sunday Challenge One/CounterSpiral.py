# problem https://www.hackerrank.com/contests/dsc-sist-competitive-coding-cookoff/challenges/counter-spiral

def spirallyTraverse(matrix, r, c): 
    min_row = 0
    min_col = 0
    
    max_row = len(matrix)-1
    max_col= len(matrix[0]) - 1
    
    total_elements = r*c
    counter = 0
    
    result = []
    while (min_row<=max_row or min_col <= max_col):
        # left wall
        for row in range(min_row,max_row+1):
            result.append(matrix[row][min_col])
            counter+=1
        min_col+=1
            
        # bottom wall
        for col in range(min_col,max_col+1):
            result.append(matrix[max_row][col])
            counter+=1
        max_row-=1
    
        # right wall
        for row in range(max_row,min_row-1,-1):
            result.append(matrix[row][max_col])
            counter+=1
        max_col-=1
            
    
        # top wall
        for col in range(max_col,min_col-1,-1):
            result.append(matrix[min_row][col])
            counter+=1
        min_row+=1
    
    return result
            
            
a=int(input())
arr=[]
for i in range(a):
    arr.append(list(map(int, input().split())))

ans = spirallyTraverse(arr,a,a)
for i in ans:
    print(i,end=" ")
