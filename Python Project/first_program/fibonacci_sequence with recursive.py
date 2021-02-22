def fibo_recursive(n):
    if n <= 1:
        return n
    return fibo_recursive(n-1)+fibo_recursive(n-2)

## for last fibonacci number
# print(fibo_recursive(6))
list=[]
nterms = 10
if nterms <= 0:
    print("Please Enter a positive integer")
else:
    print("Fibonacci sequence: ")
    for i in range(nterms):
       list.append(fibo_recursive(i))

print(list)
