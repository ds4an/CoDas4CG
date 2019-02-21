n = int(input())
d = { }
d = { }
for i in range(n):
	a, b = input().split()
	a, b = int(a), int(b)
	if t not in d :
		d[a]= b
	else :
		p[a]= b
ans = 0
for i in range(n):
	if a[i]not in d :
		d[a[i]]= i
	else :
		d[a[i]]= i
for i in a :
	if d[i]> 0 :
		t = d[i]
		a = d[i]
		if i > d :
			ans = i
print(ans)
