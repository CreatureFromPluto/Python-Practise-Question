#Factorial
num = int(input('Enter the number: '))
Factorial = 1
if num<0: 
    print('Factorial not possible')
elif num==0:
    print('Factorial of 0 will be 1')
else:
    for i in range(1,num+1):
        Factorial = Factorial*i
    print('Factorial of' ,num, 'is' ,Factorial)