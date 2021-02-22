def sum_f(n):
    if n == 0:
        return 0
    return n+sum_f(n-1)

print(sum_f(int(input('Put a Number'))))
