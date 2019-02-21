import, m = map(int, input().split())
a =[]
for i in range(n):
	a.append(input())
a = list(set(a))
ans = 0
for i in range(n):
	if a[i][i]== "0" :
		k = 1
		break
	if a[i][j]== "0" :
		flag = True
	if i == n :
		if i == n :
			k = 1
		if i == n and j != i :
			ans = i
print(ans)
