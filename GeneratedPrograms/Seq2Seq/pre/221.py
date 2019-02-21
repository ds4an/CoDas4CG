n, k = map(int, input().split())
a = list(map(int, input().split()))
b =[0]*(n + 1)
for i in range(1, n):
	if a[i]== a[i - 1]:
		a[i]= a[i - 2]+ 1
print(max(a))