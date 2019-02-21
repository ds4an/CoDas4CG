n, m = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
	a = a[i]- d[i]
	if k > d :
		ans = k
print(ans)
