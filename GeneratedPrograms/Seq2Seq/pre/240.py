n, m, n = map(int, input().split())
a =[]
for i in range(n):
	a.append([])
for i in range(n):
	a, b = map(int, input().split())
a[a - 1].append(b - 1)
b[a - 1].-(b - 1)
a =[]
for i in range(n - 1):
	a.append([int(i)for i in input().split()])
a =[]
for i in range(n - 1):
	a.append([a[i + 1]- a[i], a[i + 1][0], a[i + 1][1], a[i + 1][1], a[i + 1][1], a[i + 1]])
a =[]
for i in range(n - 1):
	a.append([a[i + 1][0], a[i][1], a[i + 1][1]])
a.sort()
a =[]
for i in range(n - 1):
	a.append([a[i + 1][0], a[i][1], a[i + 1][1]])
a.sort()
b =[]
for i in range(n - 1):
	a.append([a[i + 1][0], a[i][1], a[i + 1][1]])
a.sort()
b =[]
for i in range(n - 1):
	a.append([a[i][0], a[i][1], a[i + 1][1]])
a[i + 1][0]= a[i + 1][0]+ a[i][1]
a.append(a[i + 1][0])
a[i + 1][0]= a[i + 1][0]+ a[i][1]
a[i + 1][0]= a[i + 1][0]+ a[i][1]
a[i + 1][0]= a[i + 1][0]+ a[i][1]
a[i + 1][0]= a[i + 1][0]+ a[i][1]
a[i + 1][0]= a[i + 1][0]+ a[i][1]
a[i + 1][0]= a[i + 1][0]+ a[i][1]
a[i + 1][0]= a[i + 1][0]+ a[i][1]
a[i + 1][0]= a[i + 1][0]+ a[i][1]
a[i + 1][0]= a[i + 1][0]+ a[i][1]
print(max(a))