n, w, w = map(int, input().split())
a =[int(x) for i in input().split()]
a =[0]*(w + 1)
a =[0]*(w + 1)
for i in range(n):
	a[i]=[int(x) for x in input().split()]
	a[a[0]].append(i[1])
	a[a[1]].append(1)
a.sort()
i = 0
i = 0
while i < n :
	t = min(a[i], a[i])
	w -= a[i][0]
	i += 1
	w -= 1
	i += 1
print(ans)
