n =[]
p =[]
ans = 0
n = int(input())
for i in range(n):
	a.append(list(map(int, input().split())))
ans = 0
ans = 1
for i in range(n - 1):
	x = a[i][0]
	y = i
	while j < n and a[i][j]== a[j][j]:
		j += 1
	if count == n :
		j = 0
	if count == n and y == ans :
		ans = m
	if count == n :
		ans = m
print(ans)
