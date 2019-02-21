n = lambda : map(int, input().split())
n, m = f()
a =[]
for _ in range(m):
	a, b = f()
	a.append(a)
	a.append(b)
a =[]
b =[]
for i in range(n):
	if a[i][0]!= a[i][1]:
		a.append(a[i][1])
		a.append(a[i][1])
a.sort(key = lambda x : x[1])
a.sort(key = lambda x : x[1])
i = 0
i = 0
while i < n :
	if a[i][1]== a[i][1]:
		count += 1
	else :
		i += 1
		i += 1
print(ans)
