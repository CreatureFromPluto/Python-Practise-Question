#Function creation to accept 2 Strings and check if the letters match
def checkLet(data):
    return all([char in data[0].lower() for char in data[1].lower()])
print(checkLet(['python','ypth']))
print(checkLet(['python','ypths']))