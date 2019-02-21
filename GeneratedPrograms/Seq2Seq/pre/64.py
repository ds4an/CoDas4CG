n, m = map(int, input().split())
s =[]
for i in range(n):
	s.append(input())
s = set(s)
if len(s)< 1 :
	s.append(s)
else :
	s.append(s)
for i in range(n):
	if s[i][0]== '.' :
		print("NO")
exit()
print("YES")