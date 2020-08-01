num = int(input())
arr = []
arr1 = []
while(num  >= 0):
    if num >= 100: 
        arr1.append(num)
    arr.append(num)
    num = int(input())    

n = len(arr1)
if n==0:
    print (0)
else:
    z = min(arr1)
    print("\n")
    print(z)


