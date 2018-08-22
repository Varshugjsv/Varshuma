string=input()
string=string.split()
str1=string[0]
str2=string[1]
len1=len(str1)
len2=len(str2)
if(len1>len2):
    length=len1
    print(str1)
elif(len1<len2):
    print(str2)
else:
    length=len2
    for i in range(length):
        if(ord(str1[i])==ord(str2[i])):
           flag=1
           continue
        elif ord(str1[i])>ord(str2[i]):
           print(str1)
           flag=0
           break
        else:
           print(str2)
           flag=0
           break
    if(flag==1):
        print(str1)
