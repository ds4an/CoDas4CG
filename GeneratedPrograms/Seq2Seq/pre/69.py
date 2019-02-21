a =[]
b =[]
for i in range(int(input())):
	a.append(input())
for i in range(n):
	if a[i]!= b[i]:
		a[i]= b[i]
print(* a)