#This program simulates a password protected app access

password_bank={'sam': 1234,'smith':909090,'Ruth': 120987}
matched= False
x=0 #Loop control variable

while x<5:
    name =input('Enter Your Name: ')
    if name in password_bank:
        for i in range(0,3):
            password= input('Enter Your Password: ')
            if int(password) in password_bank.values():
                matched= True
                print('Access Granted')
                break
            else:
                print('Wrong Password. Enter Again: '+'You have'+ str(2-i)+'tries left')
    else:
        print('There is no such name in the password_bank.Try again')
    x=x+1

    if matched:
        break
