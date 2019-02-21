def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i):
            if c[j] == 'react':
                ans += 1
    print(ans)


if __name__ == '__main__':
    main()