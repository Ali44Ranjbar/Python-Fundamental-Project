def contduplicateelements(lst):
    countdict={}
    for element in lst:
        if element in countdict:
            countdict[element]+=1
        else:
            countdict[element]=1
    return countdict
mylist=[1,2,3,4,1,2,3,1,2,1]
result=contduplicateelements(mylist)
print(result)