t = int(input())
for i in range(t):
	s = input()
a = s.split()
b =[]
for i in range(len(a)):
		if(a[i]== b[i]):
			s.append(s[i])
else :
			s.append(s[i])
for i in range(len(s)):
		if(s[i]== '0'):
			s = s[: i]+ s[i :].count(,(s[i])+ 1)
else :
			s = s[: i]+ s[i :]
if(s[i]== s[i]):
				s = s[: i]+ s[i + 1 :]
else :
				s = s[: i]+ s[i + 1 :]
print(s)