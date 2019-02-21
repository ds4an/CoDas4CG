import = int(input())
a = list(map(int, input().split()))
s =[]
ans = 0
for i in range(1, n):
	if i == 0 :
		s.append(i)
	else :
		s.append(i[0])
		d.append(i[0])
ans = d[0]* d[1]
ans = 0
ans = 0
for i in range(1, n):
	if i == 0 or i == n :
		break
	d = a[0]* c[1]+ c
	ans = i + 1
	ans = ans * d[1]
	if d == 0 :
		ans = d[0]** 2 + d[1]
		ans = i + 1
print(ans)
