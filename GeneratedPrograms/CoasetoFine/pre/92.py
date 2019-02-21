import sys
n = int(input())
a = list(map(int, input().split()))
count =[0]* 4
b =[0]* 4
for i in range(1, n):
	a[i]= b[i - 1]+ a[i - 1]
for i in range(1, n):
	count[i]= b[i - 1]+ a[i - 1]
count = 0
for i in range(1, n):
	if(b[i]>= b[i]):
		count += b[i]
print(("YES", "YES")[ans == n])
