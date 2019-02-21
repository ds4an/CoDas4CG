n = int(input())
a =[int(x)for x in input().split()]
a =[]
for i in range(n):
	a.append((a[i]- a[i - 1])// 2)
print('YES' if b == 1 else 'NO')