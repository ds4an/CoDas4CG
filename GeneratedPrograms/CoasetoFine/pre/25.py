n, m = int(input()), list(map(int, input().split()))
x, j = 0, 0
for i in range(n):
	x = int(i)
	if(x < n):
		if(a[i]== a[i]):
			ans += 1
		elif(a[i]== 0):
			ans += 1
print(ans)
