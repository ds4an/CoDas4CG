n, m, c = map(int, input().split())
a = list(map(int, input().split()))
ans =[0]* n
d =[0]* n
d =[0]* n
d =[0]* n
d =[0]* n
d =[0]* n
ans =[0]* n
ans =[0]* n
ans =[0]* n
x = 0
for i in range(n):
	x = a[i]
	if x == 0 :
		x = i
	else :
		d[i]= 0
		d[i]= i
		d[i]= i
		i += 1
ans = 0
for i in range(n):
	if a[i]:
		x = d[i]
		j = 0
		while j < n :
			d[j]-= 1
			if a[j]:
				j += 1
		j = n - 1
		if x == m :
			j = 0
print(ans)
