def solve():
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())

    A = x1 == x2
    B = x3 == x4

    if A and B:
        return 0
    if A and not B:
        return 1
    if B and not A:
        return 1
    
    if ((y2 - y1) / (x2 - x1)) == ((y4 - y3) / (x4 - x3)):
        return 0
    else:
        ((y4 - y3)/(x4 - x3)) * (x - x3) + y3 = ((y2 - y1)/(x2 - x1)) * (x - x1) + y1

if __name__ == "__main__":
    print(solve())