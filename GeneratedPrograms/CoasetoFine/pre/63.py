t, n, c = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans =[]
ans = 0
for i in range(n - 1):
	l.append(a[i])
	if a[a[i]]== 0 :
		ans += 1
ans = l[: : - 1]
ans = 0
ans = 0
for i in range(n - 1):
	if a[i]> a[i + 1]:
		ans = ans + 1
print(ans)
