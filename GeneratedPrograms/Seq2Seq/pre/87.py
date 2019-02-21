a =[]
for i in range(int(input())):
	a, b = map(int, input().split())
a[a].append(b)
b[b]= 0
for i in range(n):
	a[i]= max(a[i], a[i])
print(max(a[max(a)- 2, b[max(a))]])