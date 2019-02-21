n = int(input())
a =[]
for i in range(1, k + 1):
	a.append([0]* m)
for i in range(1, k + 1):
	a, b = map(int, input().split())
if a[b - 1][b - 1]== 0 :
		a[b + 1]= max(b[b + 1][b + 1, 1])
if b[b + 1][b + 1]== 0 :
			a[b + 1][b + 1]= max(b[b + 1][b + 1, - 1])
print(max(a))