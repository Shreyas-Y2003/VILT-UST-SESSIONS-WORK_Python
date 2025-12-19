dict={}
i=1
while(i<=2):
    read=input("Network alias name:")
    readIP=(input("Enter the IP Address:"))
    i+=1
    dict[read]=readIP
for k,v in dict.items():
    print(f'Host detaila has Alias:{read} and IP address:{readIP}')
hname=input('Enter hostname to search:')
if hname in dict:
    dict['readIP']='127.0.0.1'
else:
    print("Not Present in dictionary")
print("Updated Network details",read +" "+ str(readIP))
