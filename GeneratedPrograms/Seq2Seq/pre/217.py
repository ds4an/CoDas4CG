a = int(input())
b =[]
for i in range(a):
	a, b = map(int, input().split())
a.append(a)
b.append(a)
a =[]
for i in range(n):
	a.append(s[i])
a.sort()
if a[0]== a[1]:
	print(s[0])
else :
	print(s[0], a[1])