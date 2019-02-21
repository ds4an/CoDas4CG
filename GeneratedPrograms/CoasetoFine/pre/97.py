def = int(input())
a =[int(x) for x in input().split()]
b =[0]*(n + 1)
for i in range(1, n):
	c = int(a[i])
	if c > 0 :
		a[i]= a[i - 1]+ 1
	else :
		d[i]= 1
ans = 0
for i in range(a):
	if i == 0 :
		c = 1
		break
	if a[i]== 0 :
		c += 1
print(ans)
