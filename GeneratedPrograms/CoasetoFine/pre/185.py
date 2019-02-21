n = int(input())
a = list(map(int, input().split()))
b =[]
for i in range(n):
	a.append([int(x) for x in input().split()])
d =[0]*(n + 1)
for i in range(1, n + 1):
	if a[i]** 2 + a[i - 1]> 0 :
		a[i]= a[i - 1]+ 1
	else :
		d[i]= 1
ans = 0
for i in range(n):
	if(a[i]* a[i])% 2 :
		x = a[i]
	else :
		b = a[i]
print(ans)
