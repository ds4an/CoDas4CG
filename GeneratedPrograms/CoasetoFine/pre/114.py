import = int(input())
a =[]
for i in range(n):
	a.append(input().split())
ans = 0
for i in range(n - 1):
	s = input().split()
	if(int(s[0])== 1):
		ans += 1
print(ans)
