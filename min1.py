num=int(input())
n=raw_input()
n=n.split()
number=[]
for i in range(num):
    number.append(int(n[i]))
min1=number[0]
for i in range(1,num):
    if min1>number[i]:
        min1=number[i]
print min1
