num=raw_input()
num=num.split()
num1=int(num[0])
num2=int(num[1])
for i in range(num1,num2+1):
    count=0
    for j in range(1,i+1):
        if(i%j==0):
            count=count+1
    if count==2:
        print(i),
