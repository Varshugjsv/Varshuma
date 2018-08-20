sentence=raw_input()
count=0
for i in range(len(sentence)):
    if(ord(sentence[i])>=48 and ord(sentence[i])<=57):
        count+=1
    else:
        continue
print(count)
