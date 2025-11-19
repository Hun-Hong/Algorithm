if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    A, B, C = map(int, input().split())

    one = (A+B)%C
    # two = ((A%C) + (B%C)) % C
    three = (A*B)%C
    # four = ((A%C) * (B%C)) % C
    for _ in range(2):
        print(one)
    for _ in range(2):
        print(three)