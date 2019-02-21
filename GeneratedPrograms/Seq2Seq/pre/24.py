n, k = map(int, input().split())
w =[]
for i in range(n):
	a, b = map(int, input().split())
a.append((b, a, b))
for i in range(n):
	if(i == 0):
		print(max(m[i][0], i + 1))
exit()
print(- 1)