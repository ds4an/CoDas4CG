n, k = map(int, input().split())
a =[]
for i in range(n):
	a.append([0]* n)
for i in range(n):
	for j in range(n):
		if a[i][j]== a[i][j]:
			a[i][j]= a[i][j]
print(a[n][k])