num=int(input())
n=raw_input()
n=n.split()
number=[]
for i in range(num):
    number.append(int(n[i]))
max1=number[0]
for i in range(1,num):
    if max1<number[i]:
        max1=number[i]
print max1
