n, n = map(int, input().split())
a = list(map(int, input().split()))
d = { }
for i in range(n):
	a, b = map(int, input().split())
	d = n - a
	a[l]+= 1
	a[l]-= 1
	a[l]+= 1
s = 0
for i in range(n):
	if a[i]< d :
		count = m + 1
	else :
		m = i
s = 0
for i in range(n):
	if a[i]< n :
		count = m + 1
	else :
		m = i
print(m, m)
for i in range(n - 1, - 1, - 1):
	print(i, end = " ")
