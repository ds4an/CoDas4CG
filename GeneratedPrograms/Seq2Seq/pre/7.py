a = int(input())
b =[]
for i in range(a):
	b = int(input())
a.append([a, b])
for i in range(n):
	if(a[i][0]== 0):
		print(i + 1)
break
else :
	print(- 1)