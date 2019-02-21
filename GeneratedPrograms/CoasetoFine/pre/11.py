def, m = map(int, input().split())
p =[""]*(n + 1)
p =[""]*(n + 1)
for i in range(1, n):
	p[i]= input()
k = 0
p =[]
for i in range(0, n):
	t = a[i]
	p = a[i]
	if i == 0 :
		p[i]+= 1
		s += i
	else :
		p[i]= 1
ans = 0
for i in range(n):
	if a[i]== 0 and p[i]== 0 :
		count += 1
	else :
		p[i]= 1
print(" ".join(p))
