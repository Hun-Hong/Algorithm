def bellman_ford():
    dist = [0] * (N + 1)

    for _ in range(N-1):
        for S, E, T in edges:
            if dist[S] != float("Inf") and (dist[S] + T < dist[E]):
                dist[E] = dist[S] + T
    
    for S, E, T in edges:
        if dist[S] != float("Inf") and (dist[S] + T < dist[E]):
            return "YES"
    
    return "NO"


if __name__ == "__main__":
    import sys

    input = sys.stdin.readline

    TC = int(input())

    for _ in range(TC):
        N, M, W = map(int, input().split())

        edges = []
        for _ in range(M):
            S, E, T = map(int, input().split())
            edges.append((S, E, T))
            edges.append((E, S, T))
        
        for _ in range(W):
            S, E, T = map(int, input().split())
            edges.append((S, E, -T))
        
        result = bellman_ford()

        print(result)