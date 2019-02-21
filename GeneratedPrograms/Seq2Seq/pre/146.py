for i in range(int(input())):
	n = int(input())
a =[int(i)for i in input().split()]
b =[0]*(n + 1)
for i in range(n):
		a[i]= a[i]
b =[0]*(n + 1)
for i in range(n):
		a[i]= a[i]
b[i]= b.index(b[i])
b.append(b)
a =[0]*(n + 1)
for i in range(n):
		a[i]= a[i]
b[i]= b.index(b[i])
b.append(b)
print(max(a))