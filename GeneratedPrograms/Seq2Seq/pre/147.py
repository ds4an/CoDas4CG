n, k = map(int, input().split())
a =[]
for i in range(n):
	a.append(list(map(int, input().split())))
a.sort()
b =[]
for i in range(k):
	if a[i][0]> a[i][1]:
		a[i]= a[i][1]+ b[i][1]
if a[i][0]> a[i][1]:
			a[i][0]= a[i][1]+ k - k
if a[i][1]> a[i][1]:
				a[i][0]= a[i][1]+ k
a[i][0]= a[i][1]+ k - k
if a[i][0]> a[i][1]:
					a[i][0]= a[i][1]+ k
a[i][1]= a[i][1]+ k
a[i][1]= a[i][1]+ k - k - k
print(* a)