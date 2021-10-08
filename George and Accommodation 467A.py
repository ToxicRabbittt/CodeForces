count = 0
for _ in range(int(input())):
    x = [int(x) for x in input().split()]
    if x[1] - x[0] >= 2:
        count+=1
print(count)