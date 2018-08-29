str1=raw_input()
flag=0
flag1=0
for i in str1:
    if ord(i)>=48 and ord(i)<=57:
        if flag==1:
            continue
        else:
            flag+=1
    elif ord(i)>=65 and ord(i)<=90 or ord(i)>=97 and ord(i)<=122:
        if(flag1==1):
            continue
        else:
            flag1=flag1+1
sum1=flag+flag1
if(sum1==2):
    print("Yes")
else:
    print("No")
