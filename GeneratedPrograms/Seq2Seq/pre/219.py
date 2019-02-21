n = int(input())
a =[]
for i in range(n):
	a.append(input())
a =[]
for i in range(n):
	a.append([int(i)for i in input().split()])
a =[]
for i in range(n):
	a.append([0]*(n - 1))
for i in range(n):
	if a[i][0]== 0 :
		a[i][0]= a[i][0]+ 1
a[i][0]= a[i][0]+ 1
a[i][0]= a[i][1]+ 1
a[i][0]= a[i][1]+ 1
a[i][0]= a[i][1]+ 1
a[i][1]= a[i][1]+ 1
a[i][1]= a[i][1]+ 1
a[i][1]= a[i][1]+ 1
a[i][1]= a[i][1]+ 1
a[i][1]= a[i][1]+ 1
a[i][1]= a[i][1]+ 1
a[i][1]= a[i][1]+ 1
a[i][1]= a[i][1]+ 1
a[i][1]= a[i][1]+ 1
a[i][1]= a[i][1]+ 1
a[i][1]= a[i][1]+ 1
a[i][1]= a[i][1]+ 1
a[i][1]= a[i][1]+ 1
a[i][1]= a[i][1]+ 1
a[i][1]= a[i][1]+ 1
a[i][1]= a[i][1]+ 1
a[i][1]= a[i][1]+ 1
a[i][1]= a[i][1]+ 1
print('\n'.join(a))