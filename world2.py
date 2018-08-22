string=input()
if(len(string)==1):
    if(ord(string)>=49 and ord(string)<=57):
        print("yes")
    else:
        print("no")
elif(len(string)==2):
    if(ord(string[0])==49 and ord(string[1])==48):
        print("yes")
    else:
        print("no")
