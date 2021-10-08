a = input()
b = input()
for i in range(len(a)):
    print('0', end='') if a[i] == '0' and b[i] == '0' else (print('0', end='') if a[i] == '1' and b[i] == '1' else print('1', end=''))