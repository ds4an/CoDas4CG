n = int(input())
a = list(map(int, input().split()))
p =[]
for i in range(1, n):
	t =(n - a[i])% mod
	if i > 1 :
		l.append((i, i))
ans = 1
ans = 1
for i in range(1, n + 1):
	t = sum(d[i])
	if i >= n :
		ans = i
		k = i
	if i == 1 :
		ans = i
print(ans)
