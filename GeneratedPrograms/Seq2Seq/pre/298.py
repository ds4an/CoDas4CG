n = int(input())
a =[]
for i in range(n):
	a.append(list(map(int, input().split())))
a =[0]*(n + 1)
for i in range(0, n):
	a[i]=[0]*(n + 1)
for i in range(0, n):
	a[i][0]= a[i][0]+ 1
for i in range(0, n):
	a[i][0]= a[i][0]+ 1
a[i][0]= a[i][0]+ 1
for i in range(0, n):
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
print(max(a))