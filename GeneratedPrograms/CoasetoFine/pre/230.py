s = input()
n = int(input())
d =[0]* 26
n = 0
for i in range(1, n):
	a = a.index(s[i])
	if i == 0 :
		n += 1
	elif s[i]== 1 :
		n += 1
print(n)
