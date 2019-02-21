n = int(input())
l =[int(i)for i in input().split()]
r =[]
for i in range(2, n + 1):
	if l[i]== r :
		r.append(i)
r.append(i)
r = max(l)
if r == n :
	print(max(l))
else :
	print(max(l))