t = int(input())
a =[]
for i in range(t):
	a = list(map(int, input().split()))
	a = a[0]
	count = 0
	for j in range(1, n):
		if a[j]== a[j - 1]:
			count += 1
		else :
			c = 0
ans = 0
for i in range(n):
	if a[i]== "0" :
		count = i + 1
	else :
		count = i + 1
print(ans)
