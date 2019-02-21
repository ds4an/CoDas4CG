s = input()
n = len(s)
a =[]
for i in range(n):
	for j in range(i + 2, n):
		a.append(s[i])
ans = 0
for i in range(len(s)):
	for j in range(i + 1, n):
		if s[i]== s[j]:
			count += 1
print(count)
