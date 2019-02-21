n = int(input())
a =[]
for i in map(int, input().split()):
	a.append(i)
a.sort()
i = 0
while i < n and a[i]== 0 :
	i += 1
while i * i <= n :
	if a[i]& 1 :
		i += 1
	else :
		j += 1
print(i)
