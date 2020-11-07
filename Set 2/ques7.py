def paraLine(line1,line2):
    return line1[0]/line1[1] == line2[0]/line2[1]
#first case
print(paraLine([2,3,4], [2,3,8]))
#second case
print(paraLine([2,3,4], [4,-3,8]))