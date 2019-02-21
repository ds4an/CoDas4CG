n, m, m = map(int, input().split())
a =[]
for i in range(n):
	a.append([int(x)for x in input().split()])
b =[]
for i in range(n):
	b.append([0]*(a - 1))
for i in range(1, n):
	if a[i][0]< a[i - 1][0]:
		b[i][0]= a[i - 1][1]- a[i][1]
b[i][1]= a[i - 1][1]
b[i][1]= a[i - 1][1]
b[i][1]= a[i - 1][1]
b[i][1]= a[i - 1][1]
b.append([a[i - 1][1], b[i - 1][1]])
if a[i][0]- a[i - 1][0]- a[i - 1][0]- a[i - 1][0]- a[i - 1][0]- a[i - 1][0]< a[i][1]:
			b[i][0]= a[i - 1][1]- a[i][1]
b.append((a[i - 1][0], a[i][1]))
print(* a)