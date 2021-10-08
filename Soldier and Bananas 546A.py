k, n, w = map(int, (input().split()))
totalsum = 0
for i in range(1,w+1):
    totalsum+=k*i
print(totalsum-n) if totalsum-n>0 else print(0)
