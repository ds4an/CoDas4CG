n = input()
n = len(s)
i = 0
k = 0
l =[]
for i in range(n):
	s = input()
	l.append(s)
for i in range(len(s)):
	if s[i]== "a" :
		count += 1
	else :
		k += 1
if k == n :
	print("-1")
	print(ans)
else :
	print("-1")
