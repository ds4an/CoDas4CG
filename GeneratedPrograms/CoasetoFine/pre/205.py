n = int(input())
a =[]
b =[]
for i in range(n):
	a.append(list(map(int, input().split())))
a =[]
ans =[]
for i in range(n):
	a.append(a[i])
	if a[i]!= t :
		ans.append(i)
ans = 0
ans = 0
for i in range(n):
	x = a[i]
	if x == n :
		f = 0
		break
if f :
	print("YES")
else :
	print("NO")
