n = int(input())
t =[]
for i in range(n):
	t = input()
	count = 0
	for j in range(0, len(t)- 1):
		if t[j]in d :
			t.insert(i + 1, i + 1)
		else :
			count = c + 1
	if t[i]== s :
		t = t[: t[i][: : - 1]]
print(ans)
