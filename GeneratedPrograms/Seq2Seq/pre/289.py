n, a = map(int, input().split())
a =[]
for i in range(n):
	a.append(list(map(int, input().split())))
a = a[0][0]- a[0][0]
for i in range(1, n):
	a[i][0]= a[i - 1][0]- a[i - 1][0]- a[i - 1][0]
for i in range(n - 1):
	a[i + 1][0]= a[i + 1][0]- a[i][1]- a[i][1]
a[i + 1][0]= a[i + 1][0]- a[i][1]- a[i][1]
print(max(a))