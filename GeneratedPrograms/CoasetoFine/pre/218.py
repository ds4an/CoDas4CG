n, m, c = 0, 0, 0
for i in range(int(input())):
	a, y = map(int, input().split())
	x, y = a - a, y - y
	if y == 0 :
		if y == 0 :
			s = 0
		elif a == 0 :
			y = 0
	elif a == 0 :
		y = 1 - a
	if y == 0 :
		ans = 0
	if a == 0 :
		ans = 0
print(ans)
