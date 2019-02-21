n = int(input())
a =[]
for i in range(n):
	a.append(list(map(int, input().split())))
ans = 0
for i in range(q):
	n = int(input())
	s = n - a
	if(a % 2 == 0):
		s = n // 2
	else :
		s = s
print(ans)
