n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
s = 0
for i in range(n):
	if a[i]== a[i - 1]:
		s += a[i]
else :
		s = a[i]
print(s)