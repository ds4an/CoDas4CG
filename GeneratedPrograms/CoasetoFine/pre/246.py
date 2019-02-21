t = input()
k = int(input())
a = list(map(int, input().split()))
ans = 0
ans = 0
for i in a :
	if i % 2 :
		ans += i *(i - i)
	else :
		ans += i *(n // i)
print(ans)
