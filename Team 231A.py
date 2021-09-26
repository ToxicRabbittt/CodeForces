count = 0
for _ in range(int(input())):
    l = [int(x) for x in input().split()]
    if l.count(1)>1:
        count+=1
    else:
        count+=0
print(count)
