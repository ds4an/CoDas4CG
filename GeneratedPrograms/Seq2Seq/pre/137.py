n = int(input())
a =[int(x)for x in input().split()]
a =[0]*(n + 1)
b =[0]*(n + 1)
for i in range(n):
	if a[i]== 0 :
		a[i]= a[i - 1]+ 1
else :
		a[i]= a[i - 1]+ 1
if a[i - 1]== a[i - 1]:
			a[i]= a[i - 1]+ a[i - 1]
a[i]= a[i - 1]+ a[i - 1]
print(a[0], a[1])