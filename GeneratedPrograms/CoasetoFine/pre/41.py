n = lambda : map(int, input().split())
n, k, d = f()
a =[0]* n
s = 0
for i in range(n):
	c = 0
	b = i - 1
	b = 0
	for j in range(n - 1):
		if a[j]* 2 - a[j]<= a[j]:
			c = b - 1
			b = j - 1
			break
	if s :
		d = b - 1
		c = 0
		while j < n and a[j]<= d :
			j += 1
		s += a[j]
	if d == 0 :
		d = 0
		d = 0
print(d)
