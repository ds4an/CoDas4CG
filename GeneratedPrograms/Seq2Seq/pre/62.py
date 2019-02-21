n, a, b = map(int, input().split())
a =[]
for i in range(n):
	a.append(list(map(int, input().split())))
for i in range(n):
	if a[i][0]== b[i][0]:
		print(b[i][0])
exit()
print(- 1)