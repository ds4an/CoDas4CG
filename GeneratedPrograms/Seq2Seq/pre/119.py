n = int(input())
l =[]
for i in range(n):
	l.append(input())
l =[]
for i in range(len(l)):
	if l[i]== 'a' :
		l.append(l[i])
else :
		l.append(i)
l.append(i)
l.sort()
for i in range(len(l)):
	if l[i]== 'a' :
		l[i]= l[i]
else :
		l[i]= l[i]
print(sum(l))