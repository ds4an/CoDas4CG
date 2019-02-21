n, n = map(int, input().split())
a =[int(x)for x in input().split()]
a =[0]*(n + 1)
b =[0]*(n + 1)
for i in range(1, n):
	a[i]=(a[i - 1]- 10 * 10)-(10 ** 9 - 10 ** 9)- 10 ** 9
a[i]= 0
for i in range(n):
	if a[i]== 10 ** 9 :
		a[i]= 0
a[i]= 0
else :
		a[i]= 0
for i in range(n):
	if a[i]== b[i]:
		a[i]= 0
else :
		a[i]= 0
for i in range(n):
	if a[i]== 10 ** 9 :
		a[i]= 0
else :
		a[i]= 0
for i in range(n):
	if a[i]== b[i]:
		print(n)
break
else :
	print(0)