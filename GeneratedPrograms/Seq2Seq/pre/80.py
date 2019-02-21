n, m = map(int, input().split())
a = list(map(int, input().split()))
b =[0]* n
for i in range(n):
	for j in range(n):
		if a[i]> a[j]:
			a[j]= a[j]
b[j]= a[j]
for i in range(n):
	if a[i]> a[j]:
		j = 0
for j in range(n):
			if a[j]> a[j]:
				a[j]= a[j]+ 1
a[j]= a[j]+ 1
a[j]= a[j]+ 1
a[j]= a[j]+ 1
a[j]= a[j]+ 1
a[j]= a[j]+ 1
a[j]= a[j]+ 1
a[j]= a[j]+ 1
print(len(a))
for i in a :
	print(i, end = ' ')