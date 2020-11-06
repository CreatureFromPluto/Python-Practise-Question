#Fibonacci Series
def fibSeries(n):
    if n == 1:
        return[0]
    elif n == 2:
        return[0,1]
    else:
        x = fibSeries(n-1)
        x.append(sum(x[:-3:-1]))
        return x
x = fibSeries(10)
print(x)

#Multiple of 5
listA = []
def mulof5():
    for i in range(5,51,5):
        print(i)

#Negative numbers
def negative():
    for b in range(-1,-11,-1):
        print(b)
print('Pick the Function')
print('1')
print('2')
print('3')

select = input('Enter the Function to use:')
if select == '1':
    print(x)
elif select == '2':
    mulof5()
elif select == '3':
    negative()