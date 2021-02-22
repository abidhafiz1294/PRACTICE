my_tech=['iphone','android', 'asus laptop', 'monitor']

print('Enter a tech name: ')
name=input()
if name.lower() not in my_tech:
    print('Nope its not in the list .')
else:
    print(name + ' is my tech')
