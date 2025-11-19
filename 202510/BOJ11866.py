from collections import deque

if __name__ == "__main__":
    N, K = map(int, input().split())

    queue = deque([number for number in range(1, N + 1)])
    
    series = []
    while queue:
        queue.rotate((K-1)*-1)
        series.append(queue.popleft())
    
    print("<", end="")
    print(", ".join(map(str,series)), end="")
    print(">")
