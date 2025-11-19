if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    N = int(input())

    W = [list(map(int, input().split())) for _ in range(N)]

        
    dp = [[float("Inf")] * N for _ in range(1 << N)] 

    dp[1][0] = 0
    
    for mask in range(1 << N):
        for last in range(N):
            if dp[mask][last] == float("Inf"):
                continue

            for next in range(N):
                if mask & (1 << next):
                    continue
                if W[last][next] == 0:
                    continue

                dp[mask | (1 << next)][next] = min(dp[mask | (1 << next)][next], dp[mask][last] + W[last][next])

    result = float("Inf")

    for last in range(N):
        if W[last][0] == 0:
            continue
        
        result = min(result, dp[(1 << N) - 1][last] + W[last][0])
    
    print(result)
