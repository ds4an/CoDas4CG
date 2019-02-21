n = int(input())
a = list(map(int, input().split()))
ans = 5
for i in range(n):
	c = 1
	for j in range(n):
		if a[i]== b[j]:
			k += 1
		else :
			ans += 1
print(ans)
