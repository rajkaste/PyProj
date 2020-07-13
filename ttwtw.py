def solution(xs):

    zero=filter(lambda x:x!=0, xs)
    zlist=list(zero)
    if not zlist:
        return ("0")

    count = len(xs)
    if count == 1:
        return str(xs[0])

    elif count == 0:
        return ("0")

    list1= filter(lambda x:x<0, xs)
    list2 = list(list1)

    if list2:    
        maximum=max(list2)
    count2 = len(list2)
    count1 = len(zlist)
    if count2 == 1 and count1 == 1:
        return str(list2[0])  
    if (count == 2 and count2 == 1) :
        return str(max(xs))      
    res = 1
    for i in xs:
        if i!=0:
            res=res*i
        
    if res>0:
        return (str(int(res)))
    else:
        res= int(res/maximum)
        return (str(res))

print(solution([2,3]))
print(solution([-2,3]))
print(solution([2,-3]))
print(solution([-2,-3]))
print(solution([0,3]))
print(solution([3,0]))
print(solution([0,-3]))
print(solution([-3,0]))