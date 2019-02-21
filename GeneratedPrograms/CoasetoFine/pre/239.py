t = a
a = list(map(int, input().split()))
t =[0]*(n + 1)
t =[0]*(n + 1)
for i in range(1, n + 1):
	if s[i]:
		t[i]= t[i - 1]+ 1
	else :
		t[i]= 0
ans = 0
for i in range(1, n + 1):
	if s[i]:
		count += 1
ans = 0
for i in range(n):
	if s[i]== 0 :
		count += 1
print(count)
