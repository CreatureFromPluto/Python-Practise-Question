#Creation of funtion to find largest product
def productNum(data):
    return max(a*b for a,b in zip(data,data[1:]))
print(productNum([1,2,3,4,5,6]))
print(productNum([1,2,3,4,5]))