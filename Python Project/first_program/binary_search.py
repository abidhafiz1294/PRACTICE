def linear_search(some_list,value):
    first=0
    last= len(some_list)-1
    while first <= last:
       mid=(first+last)//2
       if some_list[mid]==value:
           return 'FOUND'
       elif some_list[mid] > value:
           first=mid+1
       elif some_list[mid] > value:
           last=mid -1
    if first > last:
        return 'Not FOUND'
f=[1,2,3,4,5,6]
print(linear_search(f,5))
