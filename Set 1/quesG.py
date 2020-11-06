num = []
for i in range(8):
    a = int(input('Enter the numbers :'))
    num.append(a)
#Sorting
num.sort()
#Median
if len(num)%2 ==0:
    first_med = num[len(num)//2]
    second_med = num[len(num)//2-1] 
    median = (first_med + second_med)/2
else:
    median = num[len(num)//2]
print(num)
print(str(median))