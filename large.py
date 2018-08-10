num=int(input())
num1=raw_input()
num1=num1.split()
num2=int(num1[0])
num3=int(num1[1])
num4=int(num1[2])
if num2>num3 and num2>num4:
    print(num2)
elif num3>num2 and num3>num4:
    print(num3)
else:
    print(num4)
