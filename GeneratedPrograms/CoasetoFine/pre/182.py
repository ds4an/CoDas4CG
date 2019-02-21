n, k = map(int, input().split())
a = list(map(int, input().split()))
b =[]
a.append(0)
b.append(0)
ans = 0
for i in range(n):
	b.append(a[i]+ b[i])
	if i == 0 :
		j = 0
		b = i
if s == 0 :
	print(a[n - 1])
else :
	print(a[n - 1]+ a[n - 1])
