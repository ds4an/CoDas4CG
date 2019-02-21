n, k, d =[int(x) for x in input().split()]
a =[]
for i in range(n):
	a.append([0, 0])
ans = 0
for i in range(1, n + 1):
	if a[i][i - 1]== 0 :
		count += 1
	if count == d :
		count = 0
		count = 0
		count = 0
		count = 0
		count = 0
		while i < n and a[i][j]== a[i + 1][j]:
			count += 1
		i += 1
	if count == n :
		f = 0
		break
if ans == n :
	print("YES")
else :
	print("NO")
