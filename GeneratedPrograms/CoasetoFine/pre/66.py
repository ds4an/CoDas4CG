n = int(input())
a = list(map(int, input().split()))
r = 0
r = 0
for i in range(1, n):
	if a[i]== a[i - 1]:
		ans += 1
	else :
		r += 1
print(n / n)
