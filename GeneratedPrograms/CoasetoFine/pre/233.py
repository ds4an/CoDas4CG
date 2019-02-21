n = int(input())
d =[[]for i in range(0)]
for i in range(n):
	a, b, c = map(int, input().split())
	d[a].append(y)
	d[y].append(a)
s =[0]* n
ans = 0
for i in range(n):
	d[a[i]][i]+= s[i]
	if s[i]== s[i]:
		p = s[i]
for i in range(10):
	if s[i]== 0 :
		x = s[i]
		ans = 1
		while s[j]== s[i]:
			j += 1
		s[i]+= 1
		if s[j]== s[i]:
			x = s[j]
print("YES" if ans else "-1")
