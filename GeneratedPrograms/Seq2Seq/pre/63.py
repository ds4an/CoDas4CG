n, k = map(int, input().split())
n = int(input())
k = 0
for i in range(n):
	k =(n + i * k)% 2
if n % 2 == 0 :
		k *= 2
print(k // 2)