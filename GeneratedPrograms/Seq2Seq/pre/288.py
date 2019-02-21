n, a = map(int, input().split())
a =[0]*(n + 1)
b =[0]*(n + 1)
b =[0]*(n + 1)
for i in range(n):
	a, b = input().split()
b = int(b)
b[b]= b.get(b, 0)+ 1
a[a]= b.get(b, 0)+ 1
print(max(b))