n = input()
n = len(s)
ans = 0
ans = 0
ans =[]
for i in range(0, n):
	x = s + s[i]
	if l >= 0 :
		ans.append(i)
ans = 0
for i in range(len(s)):
	ans = i + 1
	if s[i]== - 1 :
		count = count + 1
if count == - 1 :
	print(ans)
else :
	print(n - l)
