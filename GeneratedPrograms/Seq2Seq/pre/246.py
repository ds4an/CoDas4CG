n, k = map(int, input().split())
a =[]
for i in range(n):
	a.append([])
for i in range(n):
	a.append([int(x)for x in input().split()])
a.sort()
b =[]
for i in range(len(a)):
	if a[i][0]== a[i][1]:
		a[i]= a[i][1]- a[i][1]
else :
		a[i]= a[i][1]- a[i][1]
if a[i][0]== a[i][1]:
			a[i]= a[i][1]- a[i][1]
print(a.count(a[- 1]))