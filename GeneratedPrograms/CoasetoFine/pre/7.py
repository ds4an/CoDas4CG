def = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
for i in range(n):
	if(a[i]> c):
		c = count + 1
if(c == 0):
	print(ans)
else :
	print(- 1)
