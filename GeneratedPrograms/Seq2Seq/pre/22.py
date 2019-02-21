n, x = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(n):
	if a[i]== b[i]:
		print(i + 1)
break
else :
	print(0)