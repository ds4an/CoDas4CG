n, a = map(int, input().split())
s =[]
for i in range(n):
	s = list(map(int, input().split()))
s.append(s)
for i in range(n):
	s = sum(a[i])
if s[i]== s[i]:
		s = s + 1
print(s)