n, m = map(int, input().split())
a = list(map(int, input().split()))
b =[]
for i in range(n):
	a.append(input())
a =[]
for i in range(n):
	if a[i]== b[i]:
		a.append(a[i])
else :
		a.append(a[i])
print(len(a))
print(* a)