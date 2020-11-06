# Addition
def add(n1, n2):
    return n1 + n2

#Subtraction
def sub(n1, n2):
    return n1 - n2

#Multiplication
def mult(n1, n2):
    return n1 * n2

#Divison
def div(n1, n2):
    return n1 / n2
print('Pick the operation')
print('+')
print('-')
print('*')
print('/')

select = input('Enter the Operator to use:')
n1 = float(input('Enter the first no.: '))
n2 = float(input('Enter the other no.: '))
if select == '+':
    print(n1,'+',n2,'=', add(n1, n2))
elif select == '-':
    print(n1,'-',n2,'=', sub(n1, n2))
elif select == '*':
    print(n1,'*',n2,'=', mult(n1, n2))
elif select == '/':
    print(n1,'/',n2,'=', div(n1, n2))
else:
    print('Error')
