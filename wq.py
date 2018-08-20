sentence=raw_input()
count=0
for i in range(len(sentence)):
    if(ord(sentence[i])>=58 and ord(sentence[i])<=64 or ord(sentence[i])>=91 and ord(sentence[i])<=96 or ord(sentence[i])>=123 and ord(sentence[i])<=126):
        count+=1
    else:
        continue
print(count)
