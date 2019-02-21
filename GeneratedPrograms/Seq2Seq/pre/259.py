a = int(input())
b =[]
for i in range(a):
	b = input()
a.append([a, b])
for i in range(n):
	if a[i][0]== b[i][1]:
		print(i + 1)
break
else :
	print(- 1)