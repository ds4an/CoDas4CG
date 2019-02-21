n, p = map(int, input().split())
a =[0]* 10
for i in range(n):
	a, b = map(int, input().split())
if a[a]== 1 :
		a[a]= 1
else :
		a[a]= 1
for i in range(n):
	for j in range(i + 1, n):
		if a[i]== b[j]:
			a[i]= a[j]+ 1
print(sum(a))