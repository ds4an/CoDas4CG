import = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(w):
	x = i - 1
	if a[i]== x :
		ans = k + 1
print(ans)
