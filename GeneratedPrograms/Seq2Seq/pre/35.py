import math
n, a = map(int, input().split())
a = list(map(int, input().split()))
a =[]
for i in range(3):
	a.append(a[i])
for i in range(3, n + 1):
	if a[i]== n :
		a[i]= a[i]
print(* a)