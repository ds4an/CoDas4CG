n, m = map(int, input().split())
a =[list(map(int, input().split())) for i in range(n)]
d =[[]for i in range(n)]
for i in range(1, n + 1):
	x = 0
	y = 0
	for j in range(1, n + 1):
		if a[i]:
			count += 1
			d[i]= a[i - 1]+ 1
	if a[i]> a[i]:
		ans = True
if f :
	print("YES")
else :
	print("-1")
