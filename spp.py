sentence=raw_input()
count=0
for i in range(len(sentence)):
    if(ord(sentence[i])==46):
        count+=1
    else:
        continue
print(count+1)
