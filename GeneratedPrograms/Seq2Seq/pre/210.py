n, a, b = map(int, input().split())
a = list(map(int, input().split()))
b =[]
for i in range(n):
	a.append(int(input()))
a.sort()
b.sort()
if a[0]== a[1]:
	print(- 1)
exit()
for i in range(1, n):
	if a[i]== a[i - 1]:
		print(i + 1)
break
else :
	print(- 1)