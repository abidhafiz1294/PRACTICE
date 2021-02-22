print('Input a year:')
year = int(input())
if year%400==0:
    print('this is a leaper year')
elif year%100 == 0:
    print('this is not a leaper year')
elif year%4==0:
    print('this is a leaper year')
else:
    print('this is not a leaper year')
