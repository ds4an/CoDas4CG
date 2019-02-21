n = int(input())
a =[]
for i in range(n):
	a.append([])
for i in range(n):
	a.append(list(map(int, input().split())))
for i in range(n):
	if a[i][0]== 0 :
		print(i + 1)
break
else :
	print(- 1)