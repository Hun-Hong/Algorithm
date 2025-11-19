if __name__ == "__main__":
    import sys
    input = sys.stdin.readline


    N, M = map(int, input().split())

    height = list(map(int, input().split()))

    left_h = 0
    right_h = max(height)
    
    while left_h <= right_h:
        mid = (left_h + right_h) // 2

        total = sum(h - mid for h in height if h > mid)

        if total >= M:
            result = mid
            left_h = mid + 1
        elif total < M:
            right_h = mid - 1
    
    print(result)