n = int(input())
a = list(map(int, input().split()))
d =[0]* n
count = 0
for i in range(n):
	d[a[i]]+= 1
	if d[a[i]]<= d[d[i]]:
		count += 1
print(count)
