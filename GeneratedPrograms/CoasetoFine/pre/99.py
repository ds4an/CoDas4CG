t, q = int(input()), list(map(int, input().split()))
t =[i for i in t if i <= q]
t =[i for i in t if i <= q]
for i in range(q):
	t = t[i]
	for j in range(m):
		if t[j]== l :
			arr.append(j)
print(ans)
