n = int(input())
d = { }
for i in range(n):
	a, b = input().split()
	x = int(x)
	y = int(y)
	if t not in d :
		d[a]= 1
	else :
		d[x]= 1
ans = 0
for i in range(n):
	if len(d[i])== 0 :
		count += 1
print(" ".join(map(str, ans)))
