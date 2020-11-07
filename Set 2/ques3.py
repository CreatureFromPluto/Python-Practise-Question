side1 = int(input('Enter the size of first side :'))
side2 = int(input('Enter the size of second side :'))
side3 = int(input('Enter the size of third side :'))
def rightTri(side1,side2,side3):
    a,b,c = side1**2, side2**2, side3**2
    if max(a,b,c) == (a+b+c - max(a,b,c)):
        print('YES')
    else:
        print('NO')
rightTri(side1,side2,side3)