n = int(input())
a =[int(i)for i in input().split()]
a =[]
for i in range(n):
	a.append(0)
for i in range(1, n):
	if a[i]== a[i - 1]:
		a[i]= a[i - 1]+ 1
else :
		a[i]= a[i - 1]+ 1
if a[i]== a[i - 1]:
			a[i]= a[i - 1]+ 1
print(max(a))