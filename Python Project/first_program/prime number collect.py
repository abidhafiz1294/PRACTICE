def last_number(n):
    if n==0:
        return 0
    else:
        for i in range(2,n+1):
            for j in range(2,i):
                if (i%j) ==0:
                    break
            else:
                print(i)


print('Last Number')
last_number(int(input()))
