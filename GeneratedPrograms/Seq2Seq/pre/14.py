n, a, b = map(int, input().split())
a =[]
for i in range(n):
	a.append(list(map(int, input().split())))
a =[]
for i in range(n):
	if a[i][0]== a[i][1]:
		a.append([a[i], a[i][1], i + 1])
else :
		a.append([a[i], a[i][1], i + 1])
for i in range(n):
	if a[i][0]== 0 :
		print(i + 1)
break
else :
	print(- 1)