n = int(input())
a =[int(x)for x in input().split()]
for i in range(2, n):
	a[i]= a[i - 1]
for i in range(2, n):
	a[i]= a[i - 1]+ a[i]
for i in range(2, n):
	print(a[i], end = ' ')