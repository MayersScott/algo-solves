def main():
    n = int(input().strip())

    dp0, dp1, dp2 = 1, 0, 0

    for _ in range(n):
        ndp0 = dp0 + dp1 + dp2
        ndp1 = dp0
        ndp2 = dp1
        dp0, dp1, dp2 = ndp0, ndp1, ndp2

    print(dp0 + dp1 + dp2)

if __name__ == "__main__":
    main()
