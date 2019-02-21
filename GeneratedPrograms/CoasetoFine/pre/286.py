n = input()
n = int(input())
p =[]
for i in range(0, n):
	a.append(list(map(int, input().split())))
a = sorted(l)
p = sorted(l)
ans =[0]*(n + 1)
ans =[0]*(n + 1)
for i in range(1, n):
	a[i]= a[i - 1]+ a[i]
	if a[i]>= p :
		a[i]= 1
	if a[i]>= p :
		a[i]+= 1
ans = sorted(l)
ans = sorted(ans)
ans = sorted(ans)
if k > p :
	print("YES")
else :
	print("NO")
