import math
def check_prime(n):
    flag=False
    for i in range(2,math.floor(math.sqrt(n)+1)):
        if n% i==0:
            print('The number is not prime')
            break
        flag=True
    if flag :
        print('The number is prime')

n=int(input('Input a Number'))
check_prime(n)
