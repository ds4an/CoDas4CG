n, m = map(int, input().split())
a = list(map(m, input().split()))
b = list(map(m, input().split()))
a.sort()
for i in range(m):
	if a[i][0]< a[i][0]:
		print("YES")
break
else :
	print("NO")