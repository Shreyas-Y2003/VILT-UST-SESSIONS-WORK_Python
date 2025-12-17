pin_num=[]
pin=1234
i=1
while i<=3:
    read=int(input("Enter key number"))
    
    i+=1
    if read==pin:
        pin_num.append(read)
        print("Pin Success ")
        break
    else:
        pin_num.append(f'Failed -input pin{read}')
if(read!=pin_num):
   print("All 3 attempts failed")
    
choice=input('Wish to read/see user pin details:')
choice.lower()
if(choice=='y' or choice=='n'):
    for var in pin_num:
        print(var)
