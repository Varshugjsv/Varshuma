num=raw_input()
num=num.split()
num1=int(num[0])
num2=int(num[1])
for i in range(num1,num2):
    temp=i
    sum=0
    while(temp!=0):
        rev=temp%10
        sum=sum+(rev*rev*rev)
        temp=temp/10
    if i==sum:
        print(i),
