a = 0
count = 0
for i in range(int(input())):
    temp = int(input())
    if a != temp:
        count+=1
    a = temp
print(count)