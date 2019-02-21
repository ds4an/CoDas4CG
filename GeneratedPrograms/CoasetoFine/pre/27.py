a = int(input())
for i in range(t):
	n = int(input())
	a = list(input().split())
	a =[]
	for i in a :
		if i not in d :
			a.append(i)
	a.sort(reverse = True)
	ans = 0
	i = 1
	while i < n :
		if a[i]== e :
			i += 1
		else :
			j += 1
		i += 1
	if count == 0 :
		print("YES")
	else :
		print(ans)
