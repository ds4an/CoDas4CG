n, a, b = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b =[]
for i in range(n):
	a.append(0)
b =[]
for i in range(n):
	a.append(0)
for i in range(n):
	if a[i]> b[i]:
		a[i]= a[i]
a[i]= a[i]
if a[i]> a[i]:
			a[i]= a[i]+ 1
a[i]= a[i]+ 1
print(max(a))