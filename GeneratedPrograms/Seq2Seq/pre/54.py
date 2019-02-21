input()
a = input().split()
b =[]
for i in range(n):
	a.append(int(a[i]))
b.sort()
for i in range(k):
	print(b[i], end = ' ')