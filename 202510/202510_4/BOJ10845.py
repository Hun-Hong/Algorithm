
if __name__ == "__main__":
    from collections import deque
    import sys

    input = sys.stdin.readline
    
    queue = deque([])
    N = int(input())

    for _ in range(N):
        cmd, *value = input().split()

        if cmd == "push":
            queue.append(value[0])

        elif cmd == "pop":
            if queue:
                print(queue.popleft())
            else:
                print(-1)
        elif cmd == "size":
            print(len(queue))
        elif cmd == "empty":
            if not queue:
                print(1)
            else:
                print(0)
        elif cmd == "front":
            if queue:
                print(queue[0])
            else:
                print(-1)
        elif cmd == "back":
            if queue:
                print(queue[-1])
            else:
                print(-1)