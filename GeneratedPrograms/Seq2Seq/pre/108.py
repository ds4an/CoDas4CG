n = int(input())
a = { }
for i in range(n):
	a, b = input().split()
a[int(a)]= b
for i in range(len(a)):
	if a[i]== b[i]:
		print(i + 1)
exit()
print(- 1)