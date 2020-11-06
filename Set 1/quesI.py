max = int(input('Value of n :'))
sum = 0
for i in range(2,max+1):
    m = 2
    for m in range(2,i):
        if (int(i%m)==0):
            m = i
            break
    if m is not i:
        sum += i
print('\n Sum of all prime no. till',max, ':',sum)