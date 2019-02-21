n = int(input())
a =[int(x)for x in input().split()]
a =[]
for i in range(n):
	a.append(0)
for i in range(n):
	if a[i]== 0 :
		a[i]= a[i]
print(' '.join(map(str, a)))