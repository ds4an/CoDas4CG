n = int(input())
a =[int(i) for i in input().split()]
s =[]
d = { }
for i in range(n):
	s = a[i]
	if s in a :
		d[i]+= 1
	else :
		d[i]= 1
ans = 0
for i in range(1,(n + 1)):
	if((a[i]== a[i]):
		ans += a[i]
	else :
		ans += a[i]
print(m.format(s, s))
