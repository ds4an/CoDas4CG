n = int(input())
a =[int(x)for x in input().split()]
a =[]
for i in range(n):
	a.append(0)
for i in range(n):
	for j in range(m):
		if a[i]== a[j]:
			a[i]= a[i]+ 1
a[i]= a[i]+ 1
print(sum(a))