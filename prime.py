num=int(input())
count=0
for i in range(1,num+1):
    print(i)
    if((num%i==0)):
       count=count+1
       print(count)
print(count)
if(count<=2):
    print("yes")
else:
    print("no")
