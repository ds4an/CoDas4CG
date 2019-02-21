n = int(input())
a = list(map(int, input().split()))
b = list(input().split())
ans =[]
for i in range(n):
	a.append(a[i]+ s[i])
s = 0
for i in range(n):
	x = a[i]
	if(a[i]+ a[i])% 2 :
		s = a[i]
	else :
		b = a[i]
print(s)
