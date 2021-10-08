n, h = map(int, input().split())
l = list(map(int, input().split()))
for i in l:
    if i > h:
        n+=1
print(n)