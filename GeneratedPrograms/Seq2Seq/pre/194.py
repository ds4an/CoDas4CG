t = int(input())
for i in range(t):
	s = input()
d = { }
for i in range(1, len(s)):
		if(s[i]== s[i - 1]):
			d[s[i]]= i
else :
			d[s[i]]= 1
print(s)
print(* s)