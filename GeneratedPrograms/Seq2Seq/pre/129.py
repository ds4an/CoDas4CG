n = int(input())
a =[int(x)for x in input().split()]
a =[0]*(n + 1)
for i in range(n):
	a[i]= a[i]+ a[i]
for i in range(n):
	if a[i]== 0 :
		a[i]= a[i]+ 1
print(a[0], a[1])