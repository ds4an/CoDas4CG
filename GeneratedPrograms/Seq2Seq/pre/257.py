n = int(input())
a =[]
for i in range(n):
	a.append(input())
for i in range(len(a)):
	if a[i][0]== b[i][0]:
		print(i + 1)
break
else :
	print(- 1)