n, m = map(int, input().split())
a =[0]*(n + 1)
d =[0]*(n + 1)
d =[0]*(n + 1)
for i in range(n - 1):
	s = input().split()
	x = int(s[0])
	y = int(s[1])
	d[n][1]= n
	d[y][1]= n
ans =[0]*(n + 1)
d =[0]*(n + 1)
d =[0]*(n + 1)
for i in range(n - 1):
	x = 0
	for j in range(n - 1, - 1, - 1):
		x = a[i]
		x += 1
		if a[i]== 1 :
			a[i]= i + 1
			d[i]= n
			ans += 1
print(" ".join(map(str, ans)))
