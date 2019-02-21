n = int(input())
a = list(map(int, input().split()))
b =[0]*(n + 1)
for i in range(n):
	if a[i]> a[i]:
		a[i]= a[i]
print(max(a))