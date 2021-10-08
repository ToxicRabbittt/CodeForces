x = int(input())
count = 0
if x > 5:
    while x > 0:
        x = x-5
        count+=1
else:
    count+=1
print(count)