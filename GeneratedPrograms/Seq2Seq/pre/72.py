n, a, b = map(int, input().split())
if a == b :
	print(a)
else :
	for i in range(a, b + 1):
		if i == 0 :
			print(a, i)
break
else :
		print(a, end = " ")