t = ""
t = int(input())
for i in range(t):
	s = input().split()
	n = int(s[0])
	y = int(s[1])
	a =[]
	s =[]
	for j in range(n):
		a.append([int(x) for x in input().split()])
	ans = 0
	ans = 0
	for i in a :
		x = i[0]
		y = y[1]
		if x == y :
			count = 0
			y = y
		if a == y :
			ans = x
		if a == y :
			ans = x
	print(ans)
