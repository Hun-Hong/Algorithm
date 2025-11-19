if __name__ == "__main__":
    N, W, H = map(int, input().split())

    max_length = (W ** 2 + H ** 2) ** 0.5
    for _ in range(N):
        length = int(input())

        if length <= max_length:
            print("DA")
        else:
            print("NE")