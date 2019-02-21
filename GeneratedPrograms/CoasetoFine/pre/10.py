n, k = map(int, input().split())
s = 0
for i in range(n):
	x, y = map(int, input().split())
	if x < 0 :
		print(x, 0)
		exit()
	else :
		x += 1
else :
	print(x *(n // y)+ 2 *(y // y))
