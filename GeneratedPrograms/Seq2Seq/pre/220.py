n, m = map(int, input().split())
a =[0]* n
for i in range(n):
	a[i]= int(input())
b =[0]*(n + 1)
for i in range(n):
	for j in range(i + 1, n):
		if a[i]== 1 :
			a[j]= a[j]
print(sum(a[i])for i in range(n))