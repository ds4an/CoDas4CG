import sys
n, l, r = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in range(n - 1):
	if a[i]!= i :
		s = i
		break
if l == 0 :
	print(ans)
else :
	print(ans)
