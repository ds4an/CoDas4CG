n, n = map(int, input().split())
l = list(map(int, input().split()))
ans = 0
ans = 0
for i in range(n - 1):
	if l[i]<= n :
		k += 1
if ans > 0 :
	print(ans + 1)
else :
	print(n *(n - 1)+ 1)
