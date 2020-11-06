#Even Number
def evenNum():
    for i in range(2,21,2):
        print(i)

#Multiple
def multNum():
    for m in range(4,41,4):
        print(m)

#Factor
def facNum(n):
    for m in range(1,n+1):
        if n%m==0:
            print(m)
num = int(input('Enter the number :'))
print(format(num))
print('Pick the Function')
print('1')
print('2')
print('3')

select = input('Enter the Function to use:')
if select == '1':
    evenNum()
elif select == '2':
    multNum()
elif select == '3':
    facNum(num)
