if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n = int(input())
    m = int(input())

    adj_matrix = [[float("Inf")] * (n + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        adj_matrix[i][i] = 0

    for _ in range(m):
        a, b, c = map(int, input().split())
        adj_matrix[a][b] = min(adj_matrix[a][b], c)
    
    from pprint import pprint

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                adj_matrix[i][j] = min(adj_matrix[i][j], adj_matrix[i][k] + adj_matrix[k][j])
    
    # pprint(adj_matrix)

    for row in adj_matrix[1:]:
        print(" ".join(map(lambda x: "0" if x == float("Inf") else str(x) , row[1:])))
    