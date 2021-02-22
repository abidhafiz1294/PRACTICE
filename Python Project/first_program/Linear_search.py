def liner_search(someList,value):
    for i in range(len(someList)):
        if someList[i]==value:
            return "FOUND"
    else:
            return "NOT FOUND"

a=[1,2,3,4,5,6,7,8,9]
print(liner_search(a,65))
