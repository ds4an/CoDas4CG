def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(max(abs(a[i] - a[i]) for i in range(n)))
    print(max(a))
if __name__ == '__main__':
    main()
