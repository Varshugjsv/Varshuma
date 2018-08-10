num=raw_input()
for i in range(len(num)):
    if(ord(num[i])>=48 and ord(num[i])<=57 or ord(num[i])==46):
        flag=0
    else:
        flag=1
        break
if(flag!=1):
    print("Yes")
else:
    print("No")
    
