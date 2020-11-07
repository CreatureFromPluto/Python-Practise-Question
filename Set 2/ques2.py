num1 = int(input('Enter first number :'))
num2 = int(input('Enter second number :'))
def checkNum(num1,num2):
    reverse = 0
    num = num2
    while num >0:
        remainder = num%10
        reverse = (reverse*10)+remainder
        num = num//10
    print(num)
    if num2==num1:
        print('Reversed gives first no. ')
    else:
        print("Reversed doesn't gives first no. ")
checkNum(num1,num2)
