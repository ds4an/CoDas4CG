n = int(input())
a = list(map(int, input().split()))
b =[]
for i in range(n):
	a.append(a[i])
ans = 0
for i in range(n):
	if a[i]< d :
		ans = ans + a[i]
	else :
		y = a[i]
print(ans)
