a, b = map(int, input().split())
if a > b :
	print(
max(1, a - b)- 1)
else :
	print(0)