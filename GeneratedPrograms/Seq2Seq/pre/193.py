n, p = map(int, input().split())
a =[0]*(n + 1)
for i in range(n):
	a, b = map(int, input().split())
if a[a - 1]== a[p - 1]:
		a[a - 1]= a
print(len(a))
print('\n'.join(a))