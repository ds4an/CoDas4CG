n = int(input())
a =[int(x)for x in input().split()]
a =[0]*(n + 1)
b =[0]*(n + 1)
for i in range(2, n):
	a[i]= a[i - 1]+ a[i]
for i in range(2, n):
	a[i]= a[i - 1]+ a[i]
for i in range(2, n):
	a[i]= a[i - 1]+ a[i]
for i in range(2, n):
	a[i]= a[i - 1]+ a[i]
for i in range(2, n):
	a[i]= a[i - 1]+ a[i]
print(sum(a[i])for i in range(2, n))