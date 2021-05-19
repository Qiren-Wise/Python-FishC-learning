def lists(l1,l2):
    l3=[]
    l4=[]
    l5=[]
    len1=len(l1)
    len2=len(l2)
    for i in zip(l1,l2):
            l3.extend(list(i))
    if len1 < len2:
            l4 = l1
            l1 = l2
            l2 = l4
            len1=len(l1)
            len2=len(l2)
            for i in range(len1-len2):
                    l5.append(l1.pop()) 
    else:
        len1=len(l1)
        len2=len(l2)
        for i in range(len1-len2):
            l5.append(l1.pop())
    l3.extend(list(reversed(l5)))                            
    return l3
    
l1=[1,3,4]
l2=[1,3,4]
print(lists(l1,l2)) 


