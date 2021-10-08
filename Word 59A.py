w = input()
lower = 0
upper = 0
for i in w:
    if i.isupper():
        upper+=1
    else:
        lower+=1
print(w.upper()) if upper > lower else(print(w.lower()) if upper==lower else print(w.lower()))
    