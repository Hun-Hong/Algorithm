if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    N = int(input())

    stack = []

    for _ in range(N):
        cmd, *value = input().split()

        if cmd == "push":
            stack.append(value[0])
        elif cmd == "pop":
            if stack:
                print(stack.pop())
            else:
                print(-1)
        elif cmd == "size":
            print(len(stack))
        elif cmd == "empty":
            if stack:
                print(0)
            else:
                print(1)
        elif cmd == "top":
            if stack:
                print(stack[-1])
            else:
                print(-1)