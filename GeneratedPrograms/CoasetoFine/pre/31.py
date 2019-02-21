def = 0
p =[0]* 4
k = int(input())
for i in range(t):
	a, b = map(int, input().split())
	a[i]+= 1
	a[k]-= 1
ans = 0
for i in range(1, k + 1):
	if a[i]% 2 == 0 :
		c += 1
print(c)
