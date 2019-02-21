n = int(input())
a =[]
for i in range(m):
	a.append(list(input()))
a.sort()
for i in range(m):
	print(a[i][0], end = ' ')