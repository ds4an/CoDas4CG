n = int(input())
if n < 2 :
	print(- 1)
else :
	for i in range(n):
		if sum(
i *(i - 1)<= i for i in range(n - 1)):
			print(max(max(i, i), max(i, n)))
else :
			print(max(0, max(i, i)))