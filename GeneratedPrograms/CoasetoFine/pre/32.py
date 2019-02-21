n = int(input())
a =[]
for i in range(n):
	a.append(input())
b =["", "a", "e", "x", "x", "x", "x", "x", "x", "x", "x", "x", "o", "o", "o", "o", "o", "o", "o"]
b =[]
for i in range(n - 1):
	if a[i]== a[i + 1]:
		b.append(a[i])
for i in range(n - 1):
	if a[i]== b[i + 1]:
		print(b[i], end = "")
	else :
		print(b[i], end = "")
