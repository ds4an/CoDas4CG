n, p =[int(i)for i in input().split()]
t =[int(i)for i in input().split()]
t =[int(i)for i in input().split()]
t =[[]for i in range(n + 1)]
for i in range(n):
	for j in range(i + 1, t + 1):
		if t[i][j]== t[i][j]:
			t[i][j]= t[i][j]
t = t[i][: : - 1]
t =[]
for i in range(len(t)):
	for j in range(i + 1, t):
		t =[i for j in range(n)if t[i][j]== t[i][j]]
for i in range(n):
		t[i].append(t[i][: i])
t =[i for i in t]
t =[[]for i in range(n)]
for i in range(n):
	for j in range(i + 1, t + 1):
		t[j].append(i)
for i in range(n):
	for j in range(i + 1, t):
		t[j][i]= t[i][j]
t =[[0]* n for i in range(n)]
for i in range(n):
	for j in range(i + 1, t):
		if t[i][j]== t[i][j]:
			t[i][j]= t[i][j]
t[i][j]= t[i][j]= t[i][j]= t[i][j]= t[i][j]= t[i][j]= t[i][j]= t[i][j]= t[i][j]= t[i][j]= t[i][j]= t[i][j]= t[i][j]= t[i][j]= t[i][j]= t[i][j]= t[i][j]= t[i][j]= t[i][j]= t[i][j]= t[i][j]= t[i][j]= t[i][j]= t[i][j]= t[i][j]= t[i][j]= t[i][j]= t[i][j]= t[i][j]= t[i][j]= t[i][j]= t[i][j]= t[i][j]= t[i][j]= t[i][j]= t[i][j]= t[i][j]= t[i][j]= t[i][j]= t[i][j]= t[i][j]= t[i][j]= t[i][j]= t[i][j]= t[i][j]= t[i][j]= t[i][j]= t[i][j]= t[i][j]= t[i][j]= t[i][j]= t[i][j]= t[i][j]= t[i][j + 1]= t[i : j]+ t[i : j]+ t[i : j]+ t[i :].count(i)+ j[i :].count(i)+ k[i][j]
print('\n'.join(map(str, t)))