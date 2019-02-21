n, h = map(int, input().split())
a =[0]*(n + 1)
b =[0]*(n + 1)
for i in range(n):
	a[i]= int(input())
a[i]= 0
b[i]= 0
for i in range(1, n + 1):
	if a[i]== 0 :
		a[i]=(a[i - 1]- a[i - 1])// a[i - 1]
else :
		a[i]=(a[i - 1]- a[i])// a[i - 1]
print(a[0], a[1])