n, a = map(int, input().split())
a =[]
for i in range(n):
	a.append(list(map(int, input().split())))
a.sort()
for i in range(n):
	if a[i][0]== a[i][1]:
		print(i + 1)
break
else :
	print(- 1)