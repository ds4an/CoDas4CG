n, a = map(int, input().split())
a = list(map(int, input().split()))
b =[0]*(n + 1)
for i in range(n):
	a[i]= a[i]+ a[i]
print(* a)