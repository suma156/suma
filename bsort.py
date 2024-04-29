def bsort(l):
    n=len(l)
    for i in range(0,n):
        for j in range(0,n-i,1):
            if l[j]>l[j+1]:
                t=l[j]
                l[j=l[j+1]]
                l[j+1]
                return                
l=[40,60,50,30,80]
n=len(l)
print("print the list is:",l)
bsort(l)
print(l)
