n, a, b = map(int, input().split())
a = list(map(int, input().split()))
b =[]
for i in range(n):
	a.append(int(a[i]))
a.sort()
b.sort()
print(a[- 1])