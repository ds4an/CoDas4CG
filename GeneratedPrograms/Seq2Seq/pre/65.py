s = input()
n = int(input())
s =[]
for i in range(1, n):
	s.append(s[i])
for i in range(1, n):
	s =(s + s[i])% 2
if s > s :
		print(s[i])
else :
		print(s)