if __name__ == "__main__":
    from collections import deque
    N = int(input())

    board = [[False] * N for _ in range(N)]

    max_count = 0

    queue = deque([])

    for i in range(N):
        for j in range(N):
            queue.append((i, j, 0))
    
    