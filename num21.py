num=int(input())
num1=0
num2=1
if(num==1):
    print(num2)
else:
    print(num2,end=" ")
    for i in range(1,num):
        num3=num1+num2
        num1=num2
        num2=num3
        if(i==num-1):
            print(num3)
        else:
            print(num3,end=" ")

