names = []

#Add Students
def addStudent():
    for i in range(5):
        a = input('Enter name of the student: ')
        names.append(a)

#Removal
def getOff(name):
    names.remove(name)

addStudent()
for i in range(5):
    name = input('Enter the name:')
    getOff(name)
    print(names)