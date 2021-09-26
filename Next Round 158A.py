n,k = (map(int,input().split()))
L = [int(x) for x in input().split()]
count=0
for i in range(0,len(L)):
    if L[i]>=L[k-1] and L[i]>0 :
        count+=1
print(count)
