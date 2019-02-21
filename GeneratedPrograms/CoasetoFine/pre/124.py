n = int(input())
a =[]
for i in range(q):
	a.append(list(map(int, input().strip().split())))
arr =[]
for i in range(0, q):
	a.append(a[i - 1]+ a[i])
for i in range(1, q):
	e = a[i]
	if(i == 0):
		e = a[i]
		e = a[i]
	else :
		e = a[i]
	ans = i
print(ans)
