n, k = map(int, input().split())
a =[]
for i in range(n):
	k, a, b = map(int, input().split())
a.append((a, b, k))
k = len(k)
for i in range(n):
	if(k == len(b[i])):
		print(a[i][j], end = ' ')
else :
		print(k + 1, end = ' ')