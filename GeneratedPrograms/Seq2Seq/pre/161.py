n, a = map(int, input().split())
a =[]
for i in range(n):
	a.append(input().split())
a = 0
b = 0
for i in a :
	a = a.index(i[0])
b = a[- 1][0]
if a > b :
		a += a
print(a)