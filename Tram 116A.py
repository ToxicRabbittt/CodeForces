l = []
temp = 0
for _ in range (int(input())):
    ext, entr = map(int, input().split())
    l.append(temp-ext+entr)
    temp = temp-ext+entr
print(max(l))