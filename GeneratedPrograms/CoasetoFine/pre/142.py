from, m = map(int, input().split())
a = list(map(int, input().split()))
if a[0]== 1 :
	print(n * a[0])
else :
	a =[0]* n
	d =[0]* n
	ans =[0]* n
	ans = 0
	for i in range(n):
		if a[i]> 0 :
			d[a[i]]= i
			ans[a[i]]= i
		else :
			d[a[i]]= i
	ans = 0
	for i in range(m):
		if a[i]== 1 :
			ans = max(ans, a[i])
	print(ans)
	t -= 1
