n, a, b = map(int, input().split())
a =[]
for i in range(n):
	a.append(input())
a =[]
for i in range(n):
	a.append([int(x)for x in input().split()])
a =[]
for i in range(n):
	a.append([0]*(n - 1))
for i in range(1, n):
	if a[i][0]> a[i][0]:
		a[i][0]= a[i][0]- a[i][0]
else :
		a[i][0]= a[i][0]- 1
a[i][0]= a[i][0]- 1
a[i][0]= a[i][0]- 1
a[i][0]= a[i][0]- 1
a[i][0]= a[i][0]- 1
a[i][0]= a[i][0]- 1
a[i][0]= a[i][0]- 1
a[i][0]= a[i][0]- 1
a[i][0]= a[i][0]- 1
a[i][0]= a[i][0]- a[i][0]
print('\n'.join(a))