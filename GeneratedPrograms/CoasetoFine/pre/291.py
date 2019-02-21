n, k = map(int, input().split())
a = list(map(int, input().split()))
k = 0
k = 0
for i in range(n):
	k += a[i]
	if(k - i + 1)% k == 0 :
		k = k + 1
print(k)
