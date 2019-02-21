n, k = map(int, input().split())
a = list(map(int, input().split()))
p =[0]* 100001
for i in range(1, n + 1):
	p[i]= p[i - 1].index(i - 1)
ans = 0
for i in range(1, n + 1):
	t = p[i]
	b = p[i]
	s = p[i]
	if k == 0 :
		ans = t
print(ans)
