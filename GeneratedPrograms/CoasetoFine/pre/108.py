t = int(input())
a =[]
for i in range(n):
	a.append(list(map(int, input().split())))
x = a[0][0]
ans = 0
for i in range(n):
	x = a[i][0]
	c = a[i][0]
	if(x != 0):
		ans += 1
print(ans)
