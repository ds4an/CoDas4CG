n = int(input())
a = list(map(int, input().split()))
b = sorted(a)
ans = 0
for i in range(n):
	x = a[i]
	if(x > d):
		ans = x
print(ans)
