s = input()
s = ''
for i in s :
	if i in s :
		s = ''
break
if s.upper()== s[i :].upper():
			s = s + chr(ord(i)+ 1)
else :
			s = s + s[i]
print("YES")