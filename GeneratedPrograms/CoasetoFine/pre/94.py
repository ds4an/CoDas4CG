import math
n = int(input())
a = list(map(int, input().split()))
n = int(input())
p =[]
for i in range(1, n + 1):
	a.append(a[i])
	if a[i]< s :
		k = a[i]
		p.append(i + 1)
if n > 0 :
	print("NO")
else :
	print(a[n])
