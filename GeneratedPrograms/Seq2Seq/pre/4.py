n, q = map(int, input().split())
a =[]
for i in range(q):
	a.append(list(map(int, input().split())))
a.sort()
b =[]
for i in range(q):
	a.append([int(x)for x in input().split()])
a.sort()
b.sort()
print(a[0][1]+ a[1][1]+ a[1][1]+ a[1][1])