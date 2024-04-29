def sort():
    n=len(l)
    for i in range (0,n):
        small=l[i]
        for j in range(i,l+n):
           if i[j]<small:
            small=[j]
            temp=[j]
            i[j]=[i]
            l[j]=[i]
            l[j]=temp

    return

l=[30,50,14,20,10]
print("befor sorted",1)
sort(l)
print("after sorted",1)