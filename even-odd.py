A = [1,2,3,4,5,6,7,8,9]


evenlist = []
oddlist =[]


for i in A:
    if(i % 2 == 0):
        evenlist.append(i)
    else:
        oddlist.append(i)

print("evens:", evenlist)
print("odds:", oddlist)
