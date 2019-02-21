n, k = map(int, input().split())
l =[]
for i in range(k):
	l.append(input())
l =[0]*(k + 1)
for i in range(k - 1, - 1, - 1):
	d[i]= d[i]+ d[i]
for i in range(k - 1, - 1, - 1):
	l[i]+= d[i - 1]
ans = 0
for i in range(k - 1, - 1, - 1):
	if a[i]== 0 :
		cnt += 1
print(cnt)
