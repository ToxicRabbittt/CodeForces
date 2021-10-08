a = [int(x) for x in input().split()]
s = list(input())
d=""

while (a[1]>0):
	i=0
	while i<(len(s)-1):
		if (s[i]=='B' and s[i+1]=='G'):
			s[i],s[i+1]=s[i+1],s[i]
			i+=1
		i+=1
	a[1]-=1

for i in range(len(s)):
	d+=s[i]

print(d)