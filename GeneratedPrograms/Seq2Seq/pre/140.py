n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b =[]
for i in range(n):
	a.append([])
for i in range(n):
	a[i]=(a[i]+ b[i])// b
for i in range(n):
	a[i]=(a[i]+ b[i])// b
for i in range(n):
	print(* a[i])