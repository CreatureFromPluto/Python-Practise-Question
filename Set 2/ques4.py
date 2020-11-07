num = int(input('Enter value of N :'))
def primNum(num):
    if num<=1:
        return False
    for i in range(2,num):
        if num%i == 0:
            return False
    return True
def printPri(num):
    for i in range(2,num+1):
        if primNum(i):
            print(i)
printPri(num)