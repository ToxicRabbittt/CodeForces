n = int(input())
s = input()
temp = ''
count = 0
for i in s:
    count = count+1 if i in temp else count+0
    temp=i
print(count)