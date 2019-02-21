n =[0]* 4
for i in[0, 3, 4]:
	a[i][i]= 1
for i in range(3):
	s = input()
	s =[i for i in s]
	d =[i for i in s]
	d =[i for i in s]
	s = s[0]+ 1
	for i in s :
		d[j][j]= "."
	s = "".join(a)
	if "." in s :
		print("YES")
		exit(0)
print("NO")
