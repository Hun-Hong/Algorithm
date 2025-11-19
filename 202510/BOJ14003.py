if __name__ == "__main__":
    import bisect

    N = int(input())

    arr = list(map(int, input().split()))

    dp = []
    length = [0] * N

    for idx, number in enumerate(arr):
        pos = bisect.bisect_left(dp, number)
        if pos < len(dp):
            dp[pos] = number
        else:
            dp.append(number)
        length[idx] = pos + 1
    
    target = max(length)

    series = []

    for reverse_idx, number in enumerate(length[::-1], 1):
        idx = N - reverse_idx
        if number == target:
            series.append(arr[idx])
            target -= 1
        
        if target < 1:
            break
    
    print(len(dp))
    print(*series[::-1])