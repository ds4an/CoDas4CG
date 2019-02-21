n = int(input())
a =[input()for i in range(n)]
print(
sum(
(a[i][0]- a[i][1]for i in range(len(a)))))