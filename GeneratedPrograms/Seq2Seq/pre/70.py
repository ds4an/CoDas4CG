n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
if n > 1 :
	a.sort()
else :
	a =[0]* n
for i in range(n):
		if a[i]> a[i]:
			a[i]= a[i]
if a[i]> a[i]:
			a[i]= a[i]
print("YES")
print(' '.join(map(str, a)))