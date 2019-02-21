n = int(input())
a =[int(i)for i in input().split()]
a =[0]*(n + 1)
b =[0]*(n + 1)
for i in range(1, n):
	a[i]= a[i - 1]+ a[i]
if a[i]== 0 :
		a[i]= a[i - 1]+ 1
a[i]= a[i - 1]+ 1
a[i]= a[i - 1]+ 1
a[i]= a[i - 1]+ 1
a[i]= a[i - 1]+ a[i]
a[i]= a[i - 1]+ 1
print('\n'.join(a))