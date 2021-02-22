def exponent(x,y):
    if y == 0:
        return 1
    else:
        return x*exponent(x, y-1)

print(exponent(int(input('Enter a Number: ')),int(input('Enter The Power : '))))
