import = int(input())
a =[int(x) for x in input().split()]
b =[int(x) for x in input().split()]
d =[0]*(n + 1)
for i in range(l, n + 1):
	a[i]=(a[i - 1]+ a[i - 1])% m
ans =[]
for i in range(1, n + 1):
	ans.append(a[i - 1]+ a[i])
ans = 0
for i in range(1, n + 1):
	if(a[i]- a[i - 1])% 2 == 0 :
		ans = count + 1
	else :
		r = a[i]
print(ans)
