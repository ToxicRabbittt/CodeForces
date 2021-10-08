y = int(input())
x = y+1
while True:
    for i in range(0,10):
        if str(x).count(str(i)) > 1:
            x+=1
            break
    else:
        print(x)
        break
