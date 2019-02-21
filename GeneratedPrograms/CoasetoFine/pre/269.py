n, m = map(int, input().split())
a =[]
for i in range(n):
	a, b = map(int, input().split())
	a.append((x, b))
ans = 0
for i in range(n):
	if a[i]== 0 :
		ans += a[i]
	else :
		ans += 1
		j = a[i]
print(ans)
