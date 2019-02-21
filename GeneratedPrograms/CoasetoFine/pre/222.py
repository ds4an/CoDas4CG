n = int(input())
a = list(input())
a = list(a)
n = len(a)
n = len(a)
for i in range(n):
	a.append(a[i])
	if a[i]not in a :
		a.append(a[i])
print("".join(a))
