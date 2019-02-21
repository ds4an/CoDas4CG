t = s
s = input()
s = input()
n = len(s)
s =[]
for i in range(n):
	s.append(s[i])
ans = 0
for i in range(len(s)):
	if s[i]!= s[i]:
		j = i
		break
ans = ""
i = 0
for i in s :
	if i != "?" :
		count += 1
	else :
		ans += 1
print(ans)
