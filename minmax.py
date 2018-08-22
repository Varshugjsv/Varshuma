num=int(input())
string=input()
string=string.split()
list1=[]
for i in range(num):
    list1.append(int(string[i]))
max1=max(list1)
min1=min(list1)
print('{} {}'.format(min1,max1)) 
