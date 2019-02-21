n, b = map(int, input().split())
a =[]
count = 0
ans = 0
for i in range(n):
	a.append(list(map(int, input().split())))
ans = 0
ans = 0
for i in range(n):
	if a[i]* a[i]> 0 :
		ans = i + 1
	else :
		ans = ans + 1
if ans > 0 :
	ans = 2 * n
ans = 0
ans = 0
for i in range(l, n + 1):
	if a[i]< 0 :
		ans = i + 1
		ans = i
if ans > 0 :
	print(ans * n)
else :
	print(- 1)
