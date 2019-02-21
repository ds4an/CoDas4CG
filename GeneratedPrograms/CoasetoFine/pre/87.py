def = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
s = 0
ans = 0
s =[]
for i in range(n):
	if a[i]>= n :
		s.append(i)
		c = 1
		k = 1
		p = 1
	else :
		ans += 1
		j = 0
if t :
	s.sort()
	i = 0
	while i < n :
		if a[i]<= n :
			ans += a[i]
			i += 1
		else :
			ans += a[i]
print(ans)
