import sys
n = int(input())
a = list(input().strip())
b = input()
a =[]
for i in range(n):
	a.append(int(a[i]))
a =[]
for i in range(n):
	a.append(int(a[i]))
for i in range(n):
	if a[i]== b[i]:
		a[i]= a[i]
else :
		a[i]= 1
print('\n'.join(a))