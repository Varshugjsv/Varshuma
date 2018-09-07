str1=raw_input()
str1=str1.split()
len1=len(str1)
list1=[]
list2=[]
for i in range(len1):
    list1.append(int(str1[i]))
str2=raw_input()
str2=str2.split()
len2=len(str2)
for i in range(len2):
    list2.append(int(str2[i]))
count=0
for i in range(len(list2)):
    if(list2[i]==list1[1]):
        count+=1
print(count)
