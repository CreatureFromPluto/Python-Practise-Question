num = []
for i in range(10):
    a = int(input('Enter the number :'))
    num.append(a)
#Sorting
def sorList(num):
    num.sort()

#Binary Search
target = int(input('Enter the number to be searched :'))
def binaryNum(num):
    min = 0
    max = len(num)-1
    found = False
    while min<=max and not found:
        pos = 0
        mid = (min+max)//2
        if num[mid] == target:
            pos = mid
            found = True
        else:
            if target < num[mid]:
                max = mid-1
            else:
                min = mid+1
    print(pos,found)
binaryNum(num)

