num=raw_input()
num1=int(num)
element=raw_input()
element=element.split()
list1=[]
for i in range(num1):
    list1.append(int(element[i]))
for i in range(num1):
    print(list1[i]),
    print(i)
    
