n, h = map(int, input().split())
a = list(map(int, input().split()))
b =[0]*(n + 1)
for i in range(1, n + 1):
	a[i]=(a[i - 1]- i)% 1000000007
print(* a)