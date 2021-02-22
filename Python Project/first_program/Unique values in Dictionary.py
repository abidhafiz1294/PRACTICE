a = {1:1, 2:2, 3:1, 4:34}
#b = {}
c=[]
count = {}

for i in a.values():
    ##print(i)
    count.setdefault(i, 0)
    count[i] = count[i]+1
#print(count)
#i = 0
for k,v in count.items():
    if v == 1:
        #i = i+1
        #b.update({i:k})
        c.append(k)

print(c)
#print(b)
#for i in b.values():
 #   print(i, end=" ")
