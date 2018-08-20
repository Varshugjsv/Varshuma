sentence=raw_input()
count=0
for i in range(len(sentence)):
    if(ord(sentence[i])==32):
        continue
    else:
        count+=1
print(count)
