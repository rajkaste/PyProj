num = int(input())
arr = []
while(num >= 0):
    arr.append(num)
    num = int(input())

count = 0
count2 = 0
for i in arr:
    if (i % 2 == 0):
        count += 1 
    else:
        if count>=3:
            count2 += 1
        count=0
if count >=3:
    count2 += 1
    
print(count2)
