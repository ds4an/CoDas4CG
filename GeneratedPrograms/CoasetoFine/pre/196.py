n, v = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
ans = 0
ans = 0
ans = n
while i < n :
	if a[i]<= b :
		k = a[i]
		i += 1
	else :
		ans += b
		j = i
if k == 0 :
	print(ans)
else :
	print(min(ans, b))
