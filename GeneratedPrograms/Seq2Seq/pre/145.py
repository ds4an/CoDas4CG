n = int(input())
a =[]
for i in range(n):
	a.append(input())
a =[]
for i in range(n):
	if a[i].count(a[i])== 1 :
		a.append(a[i])
else :
		a.append(a[i])
print(len(a))
print(' '.join(map(str, a)))