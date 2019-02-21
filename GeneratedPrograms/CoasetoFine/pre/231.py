n, s = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
s = sorted(a)
s = sorted(a)
for i in range(n):
	c = 0
	for j in range(i, n):
		if a[j]> c :
			ans = c + 1
	if c < n :
		ans = k
print(ans)
