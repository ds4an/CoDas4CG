a = int(input())
b = list(map(int, input().split()))
a.sort()
b = a[0]
for i in range(1, n):
	if a(b[i]):
		print(i + 1)
break
else :
	print(max(a, b))