string=raw_input()
string=string.split()
num=int(string[0])
key=int(string[1])
list1=[]
string2=raw_input()
string2=string2.split()
for i in range(num):
   list1.append(int(string2[i]))
sum1=0
for i in range(key):
    sum1=sum1+list1[i]
print(sum1)
