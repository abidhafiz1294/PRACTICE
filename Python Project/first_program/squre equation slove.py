import  math
print ('Enter the coefficients')
a=int(input())
b= int(input())
c= int(input())
D= math.sqrt(b*b -4*a*c)
x1=(-b+D)/ (2*a)
x2=(-b-D)/(2*a)
print( x1 ,x2)
