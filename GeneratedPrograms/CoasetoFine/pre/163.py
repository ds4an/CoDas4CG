f = lambda : map(int, input().split())
n = int(input())
a = list(f())
q =[]
ans = 0
for i in range(n):
	if a[i]!= a[i]:
		q.append(i)
if len(q)== 0 :
	print(- 1)
else :
	print(- 1)
