n, m = map(int, input().split())
a =[]
for i in range(n):
	x, r = map(int, input().split())
	if x == 1 :
		a.append((x, y))
a =[]
for i in range(m):
	x, y = map(int, input().split())
	if x == 1 :
		a.append((x, y))
ans = f(m)
ans =[]
for i in a :
	ans.append(p[i])
ans = 0
for i in a :
	if i == 1 :
		count += 1
print(ans)
