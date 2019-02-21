def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(n):
        for j in range(n):
            if a[i][j] == 0 and a[i][j] == 0:
                a[i][j] = '.'
                i += 1
if __name__ == '__main__':
    main()
