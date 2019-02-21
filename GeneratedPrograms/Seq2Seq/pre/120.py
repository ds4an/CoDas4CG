t = int(input())
for i in range(t):
	s = input()
a = list(s)
b =[]
for i in a :
		a.append(i.index(a[i - 1]))
a.sort(key = lambda x : x[0])
for i in a :
		if i > a[i][0]:
			a[i]= a[i - 1][0]+ a[i - 1][0]
print(a[0][0])