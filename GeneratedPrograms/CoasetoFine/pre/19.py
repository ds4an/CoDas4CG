n = int(input())
a =[]
for i in range(a):
	a.append(input())
d =[0]*(n + 1)
for i in range(n):
	a[i]= a[i]
ans = 0
for i in range(n):
	c = a[i]
	c = d.index(i)
	if i == - 1 :
		ans += 1
print(ans)
