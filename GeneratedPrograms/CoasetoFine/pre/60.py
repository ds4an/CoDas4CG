def = int(input())
a =[]
for i in range(n):
	a.append(list(map(int, input().split())))
p =[0]* n
p =[0]* n
p =[0]* n
p =[0]* n
for i in range(n):
	x = a[i]
	b = a[i]
	if t > d :
		p[i]= x
	else :
		p[i]= 1
for i in range(n):
	x, y = map(int, input().split())
	d[x]+= 1
	p[y]-= 1
ans = 0
for i in range(n):
	x = a[i]
	if a[i]> 0 :
		ans = a[i]
		p = i
print(ans)
