n = int(input())
a = list(map(int, input().split()))
b =[]
for i in range(n):
	a.append(c[i]* a[i])
for i in range(n - 1, - 1, - 1):
	if a[i]== a[i + 1]:
		print(n - i)
exit(0)
print(n - a[n - 1])