pin_num=1234
i=1
while i<=3:
    read=int(input("Enter key number"))
    i+=1
    if read==pin_num:
        print("Pin Success ")
        
        break
if(read!=pin_num):
   print("All 3 attempts failed")
    
    