def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    for i in range(n):
        a.append(input())
    for i in range(n):
        for j in range(n):
            if a[i][j] == a[i][j] and a[i][j] == a[i + 1][j]:
                a[i][j] = a[i + 1][j]
    for i in range(n):
        print(a[i][i], end='')
    print()


if __name__ == '__main__':
    main()