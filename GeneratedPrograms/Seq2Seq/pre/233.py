n, a, b = map(int, input().split())
a =[]
for i in range(n):
	a.append([int(x)for x in input().split()])
a.sort()
for i in range(n):
	print(a[i][0], end = '')
print()