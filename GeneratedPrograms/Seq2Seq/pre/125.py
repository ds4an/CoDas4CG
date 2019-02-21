n, a, b = map(int, input().split())
a =[[0]*(n + 1)for _ in range(n)]
for i in range(n):
	a[i]=[int(x)for x in input().split()]
a.sort()
b =[[0]*(n + 1)for i in range(n)]
for i in range(n):
	if a[i][0]== a[i][1]:
		print('YES')
exit()
print('NO')