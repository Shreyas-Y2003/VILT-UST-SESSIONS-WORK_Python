i=1
while i<=3:
    lname=input("Enter login name")
    

    if lname=='root':
            print("Login success")
            break
    else:
            print("try again")
    i+=1

print("Max limit reached 3 times")