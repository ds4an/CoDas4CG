import, a, y = map(int, input().split())
a =[input() for _ in range(n)]
r =[x + 1 for x in range(n)]
c =[i + 1 for x in range(n)if a[i][y]== "."]
ans =[a[i][j], i + a[i][j], i]
for j in range(n):
	x = a[i][j], a[i][j]
	if x == c :
		print("YES")
		exit()
print("NO")
