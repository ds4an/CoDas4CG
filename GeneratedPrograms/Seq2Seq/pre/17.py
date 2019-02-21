t = int(input())
while t > 0 :
	n = int(input())
a =[int(x)for x in input().split()]
a =[0]*(n + 1)
b =[0]*(n + 1)
for i in range(1, n):
		a[i]= a[i - 1]+ a[i - 1]
if a[i - 1]== a[i - 1]:
			a[i]= a[i - 1]+ 1
a[i]= a[i - 1]+ 1
a[i]= a[i - 1]+ a[i - 1]
a[i]= a[i - 1]+ a[i - 1]
a[i]= a[i - 1]+ a[i - 1]
a[i]= a[i - 1]+ a[i - 1]
print(sum(a))