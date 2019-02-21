n = int(input())
a =[int(x)for x in input().split()]
ans = 0
for i in range(n - 1):
	if a[i]== 1 :
		ans += 1
print(ans)