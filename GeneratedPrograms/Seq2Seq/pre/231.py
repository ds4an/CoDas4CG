n, k = map(int, input().split())
s =[]
for i in range(n):
	s.append(input())
s = 0
for i in range(len(s)):
	if s[i]== s[i]:
		s += 1
print(s)