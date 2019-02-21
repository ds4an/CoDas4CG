a =[]
for _ in range(int(input())):
	a.append(int(input()))
a.sort()
for i in range(1, n):
	if a[i]> a[i - 1]:
		print(i)
break
else :
	print('NO')