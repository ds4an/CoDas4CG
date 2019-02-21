n, m = map(int, input().split())
a =[]
for i in range(m):
	a.append([])
for i in range(m):
	a, b = map(int, input().split())
a[a].append(a)
b[a].append(a)
n = n - 1
for i in range(m):
	if n[i]in[n, m]:
		print(n)
break
else :
	print(n)