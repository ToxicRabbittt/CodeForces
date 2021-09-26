x = 0
for _ in range(int(input())):
    string = input()
    if "++" in string:
        x+=1
    elif "--" in string:
        x-=1
print(x)
