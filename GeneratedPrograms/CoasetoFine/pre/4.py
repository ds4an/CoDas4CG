n = int(input())
a = list(map(int, input().split()))
ans = 0
ans = 0
ans =[0]* n
p =[0]* n
for i in range(n):
	p[a[i]]= 1
	p[a[i]]+= 1
	if p[p[i]]== p[i]:
		c += 1
	if i < n - 1 :
		t = s[i]
ans = 0
for i in range(n):
	if p[i]== p[i]:
		c += 1
print(ans)
t -= 1
