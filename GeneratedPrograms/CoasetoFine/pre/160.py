def = int(input())
for i in range(n):
	n = int(input())
	a = list(map(int, input().split()))
	ans = 0
	i = 0
	ans =[]
	for i in range(n):
		if a[i]!= 0 :
			a.append(a[i])
			k += 1
	a.append(s)
	count = 0
	ans = 0
	for i in range(n):
		if a[i]== "0" :
			count += 1
			j = 1
		else :
			count += 1
	print(ans)
