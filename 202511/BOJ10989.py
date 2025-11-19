if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    N = int(input())
    count_list = [0] * 10001
    for _ in range(N):
        number = int(input())
        count_list[number] += 1
    
    for number, count in enumerate(count_list):
        for _ in range(count):
            print(number)