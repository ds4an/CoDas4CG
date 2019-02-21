n = int(input())
s = input()
s = ""
ans = ""
for i in range(n):
	s = input().split()
	s = s[1 :]
	f = True
	if s.isdigit():
		ans = c + 1
	else :
		ans = count + 1
print(ans)
