n, n = map(int, input().split())
s = input()
c = 0
for i in range(3):
	if s[i]== c :
		s += s[i]
print(s)