n, q = int(input()), list(map(int, input().split()))
for i in range(2, n):
	for j in range(2 * i, n + 1, i):
		if p[i]== 0 :
			p[i]= 1
print(sum(p))