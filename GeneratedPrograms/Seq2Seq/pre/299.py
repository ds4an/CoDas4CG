n = int(input())
a =[int(x)for x in input().split()]
b =[]
for i in range(n):
	a.append(0)
for i in range(n):
	if a[i]== a[i]:
		a[i]= a[i]
b[i]= a[i]
print(len(a))
print(' '.join(map(str, a)))