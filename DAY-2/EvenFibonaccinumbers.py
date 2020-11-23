f = 0
s = 1
sum = 0
evensum = 0

while sum < 4000000:
    sum = f + s
    f = s
    s = sum
    if sum % 2 == 0:
        evensum += sum
print(evensum)
