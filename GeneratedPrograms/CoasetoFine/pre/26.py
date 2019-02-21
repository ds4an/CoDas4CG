n = int(input())
a =[0]* n
p =[0]* n
p =[0]* n
p =[0]* n
for i in range(n):
	x, y = map(int, input().split())
	d[i]= b
	if s[x]> 0 :
		a[x]+= 1
	else :
		d[y]= 1
ans =[]
p =[]
for i in range(n):
	x, y = map(int, input().split())
	a.append((x, y, i + 1))
a.sort(key = lambda x : x[1])
ans = 0
ans = 0
for i in range(len(a)):
	if a[i][0]< n :
		ans = a[i][1]
		ans = i
if ans == 0 :
	print("YES")
else :
	print("NO")
