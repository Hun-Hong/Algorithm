if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    
    count = 0
    N = int(input())
    for _ in range(N):
        count += int(input())
    
    count -= N - 1

    print(count)
