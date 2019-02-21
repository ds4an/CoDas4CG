n = int(input())
a =[]
for i in range(n):
	a.append(list(map(int, input().split())))
a.sort()
ans =[]
for i in range(n - 1):
	ans.append(str(a[i]))
ans.append("".join(p))
