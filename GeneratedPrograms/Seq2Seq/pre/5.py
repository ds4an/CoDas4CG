n = int(input())
a = input().split()
b =[]
for i in range(n):
	a.append(int(a[i]))
a.sort()
b = 0
for i in range(n):
	if a[i]== 0 :
		a[i]= 0
b += 1
print(b)