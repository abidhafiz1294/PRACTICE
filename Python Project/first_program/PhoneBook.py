#This program simulates a phone_book
contact_no={'Sam': 0000, 'Smith': 111,'Ron': 9876}
x=0

while x < 5:
    print('Enter your Name (Press Enter To exit): ')
    name=input()

    if name=='':
        break

    if name in contact_no:
        print('The contact number of '+name+ ' is '+ str(contact_no[name]))
    else:
        print("There is no such name in the phone_book. Do you want to add it?")
        desc= input('yse / no')

        if desc=='yes':
            print('Enter the Number: ')
            num=input()
            contact_no[name]= num
            print('Dictionary Updated.')
        elif desc=='no':
            print('Do you want to quit??')
            desc=input('yes / no')
            if desc == 'yes':
                break
            else:
                print('Keep Searching')
    x=x+1
