n, m = map(int, input().split())
a =[]
for i in range(n):
	a.append([])
for i in range(n):
	a, b = map(int, input().split())
a[a].append(b)
b[b].append(b)
n = len(a)
for i in range(n):
	if a[i][1]== a[i][1]:
		print('YES')
exit()
print('NO')