pnum=int(input('Enter a port Number'))
if pnum>5000 and pnum<6000:
    appname='demoApp'
else:
    appname='testApp'
print("App Name :",appname,"running port:",pnum)
