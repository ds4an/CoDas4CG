def main():
	s = input()
a =[]
for i in range(len(s)):
		if s[i]!= chr(ord('a')+ i):
			a.append(i)
else :
			a.append(i)
if len(a)> 1 :
		print(- 1)
return
for i in range(len(a)):
		if a[i]!= chr(ord('a')+ i):
			a[i]= chr(ord('a')+ i)
else :
			a[i]= chr(ord('a')+ 1)
print('\n'.join(a))
if __name__ == '__main__' :
	main()