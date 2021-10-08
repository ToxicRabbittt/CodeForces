n = int(input())
for i in range(1,n):
    print("I love that", end=" ") if i % 2 == 0 else print("I hate that", end=" ")

print("I love it", end=' ') if n%2==0 else print("I hate it", end=" ")

        