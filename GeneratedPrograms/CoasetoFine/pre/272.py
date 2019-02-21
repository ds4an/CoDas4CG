s = int(input())
p = { }
for i in range(n):
	s = input().split()
	a[1]= int(s[1])+ 1
	s = int(s[2])
	y = s[2]
	count = 0
	for j in range(1, n):
		if a[j]== "0" :
			count += 1
	if count == 0 :
		if a[i]== "0" :
			a[i]= a[j]
	else :
		if a[i]== "0" :
			a[i]= a[i]
if s == 1 :
	print("YES")
else :
	print("NO")
