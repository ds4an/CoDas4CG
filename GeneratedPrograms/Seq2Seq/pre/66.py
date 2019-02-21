n = int(input())
a =[int(x)for x in input().split()]
a =[]
h =[]
h =[]
for i in range(a):
	a.append(input())
a.sort()
h =[]
for i in range(1, n):
	if a[i][0]- a[i][1]== a[i][1]:
		h.append((a[i][0], a[i][1]))
a.append((a[i][0], a[i][1]))
a.sort()
h =[]
h =[]
for i in range(1, n):
	if a[i][0]- a[i][1]- a[i][1]- a[i][1]- a[i][1]- a[i][1]== a[i][1]:
		h.append((a[i][0], a[i][1]))
a.append((a[i][0], a[i][1]))
print(((((a[0][0]- a[0][1])*(2 * a[0][1])+ 1)))% 2)