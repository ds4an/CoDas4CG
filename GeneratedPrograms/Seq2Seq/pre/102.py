n = int(input())
a =[n]* n
b =[0]* n
for i in range(n):
	a, b = map(int, input().split())
a[a]= a[a]+ a[a - n], n[a - n]= a, n - n
print(min(a))