n, a, b = map(int, input().split())
a =[]
for i in range(n):
	a, b = map(int, input().split())
a.append(b)
b.append(b)
b =[]
for i in range(n):
	b.append([0]*(n - 1))
for i in range(n):
	b[i][b]= b[i][0]
b =[]
for i in range(n):
	if b[i][0]> b[i][0]:
		b.append([a[i][0]])
else :
		b.append([a[i][0]])
b.append([a[i][0]])
for i in range(n - 1):
	if b[i][0]> a[i][0]:
		b[i]= b[i + 1][0]
b[i]= b[- 1][0]
b[i]= b[- 1][0]
b[- 1][0]= b[- 1][0]
b.append([b[0][0], a[- 1][0]])
b.sort(key = lambda x : x[0])
for i in range(1, n):
	b[i][0]= b[i][0]- b[i][0]
if b[- 1][0]> a[- 1][0]:
		b[- 1][0]= b[- 1][0]- b[- 1][1]
else :
		b[- 1][0]= b[- 1][1]- b[- 1][0]
b[- 1][0]= b[- 1][1]
b[- 1][0]= b[- 1][1]
b[- 1][0]= b[- 1][1]
b[- 1][0]= b[- 1][0]
b[- 1][0]= b[- 1][1]
b[- 1][0]= b[- 1][0]
b[- 1][0]= b[- 1][1]
b[- 1][0]= b[- 1][0]
b[- 1][0]= b[- 1][1]
b[- 1][0]= b[- 1][0]- b[- 1][0]
while b[- 1][0]> 0 :
				b[- 1][0]= b[- 1][1]
b[- 1][1]= b[- 1][1]
b[- 1][1]= b[- 1][0]
b[- 1][1]= b[- 1][1]
b[- 1][1]= b[- 1][0]- b[- 1][0]
b[- 1][1]= 0
break
if b[- 1][0]> b[- 1][0]:
				b[- 1][0]= b[- 1][1]- b[- 1][0]
else :
				b[- 1][0]= b[- 1][1]- b[- 1][0]
b[- 1][1]= b[- 1][1]
b[- 1][1]= b[- 1][0]- b[- 1][0]
b[- 1][1]= 0
break
print(* a)