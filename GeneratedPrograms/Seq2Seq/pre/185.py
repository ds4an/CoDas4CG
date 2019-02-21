d = { }
for i in range(int(input())):
	a, b = map(int, input().split())
d[a]= a
d[b]= 1
d = { }
for i in range(d):
	d[i]= int(input())
d[i]= d.get(i, 0)+ 1
d[i]= d.get(i, 0)+ 1
print(' '.join(map(str, d)))