import = int(input())
arr = list(map(int, input().split()))
l = list(map(int, input().split()))
ans = 1
s = arr[0]
for i in range(1, len(arr)):
	x = arr[i]
	if s == ans :
		ans = i
		ans = i
	else :
		p = i
print(ans)
