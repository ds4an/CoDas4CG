n = int(input())
s =[input() for i in range(n)]
s =[0 for i in range(6)]
for i in range(1, n + 1):
	for j in range(6):
		a = s[i][j - 1]
		if p == 0 :
			s[i][j]= s[i - 1][j]
		else :
			s[i][j]= 1
s = 0
for i in range(1, n + 1):
	for j in range(1, n + 1):
		s = s[i][j - 1]
		if t == 0 :
			print(i + 1)
			exit(0)
print("NO")
