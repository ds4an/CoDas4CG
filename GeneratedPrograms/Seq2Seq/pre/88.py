n, m = map(int, input().split())
t = list(map(int, input().split()))
t =[]
for i in range(n):
	t.append(t[i])
t =[]
for i in range(n):
	t.append(t[i])
t =[]
for i in range(n):
	t.append(t[i])
t =[]
for i in range(n):
	t.append(t[i])
t =[]
for i in range(n):
	t.append(t[i])
t =[]
for i in range(n):
	t.append(t[i])
t =[]
for i in range(n):
	t.append(t[i])
t =[]
for i in range(n):
	t.append(t[i])
t =[]
for i in range(n):
	t.append(t[i])
t =[]
for i in range(n):
	t.append(t[i])
t =[]
for i in range(n):
	t.append(t[i])
t =[[0]* m for i in range(n)]
for i in range(n):
	t[i][1]= max(t[i][0], t[i][1])
for i in range(n):
	t[i][1]= max(t[i][0], t[i][1])
for i in range(n):
	t[i][1]= max(t[i][0], t[i][1])
print('\n'.join(t))