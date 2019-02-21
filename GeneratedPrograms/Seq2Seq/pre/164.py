n = int(input())
l =[int(x)for x in input().split()]
l =[0]*(n + 1)
l = 0
r = 0
for i in range(0, n):
	if l[i]> 0 :
		r += 1
else :
		r[i]= 1
r += 1
if l[i]> 0 :
		l[i]= l[i - 1]+ 1
l[i]= l[i - 1]+ 1
l[i]= l[i - 1]+ 1
l[i]= l[i - 1]+ 1
l[i]= l[i - 1]+ 1
l[i]= l[i - 1]+ 1
l[i]= l[i - 1]+ 1
l[i]= l[i - 1]+ 1
l[i]= l[i - 1]+ 1
print('\n'.join(l))