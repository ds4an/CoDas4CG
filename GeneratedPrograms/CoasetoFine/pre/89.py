n, r = input().split()
n = int(n)
b = int(r)
s = input().split()
a =[]
for i in range(n):
	a.append(int(s[i]))
n = int(input())
s = input().strip().split()
ans =[]
for i in range(n):
	a.append(s[i])
n = int(input())
ans = 1
for i in range(n):
	n = int(input())
	s = a[n]
	q = s[n]
	if s == r :
		print("YES")
		exit()
print("YES")
for i in range(n):
	print(s[i][0], end = " ")
