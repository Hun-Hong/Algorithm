import heapq

def dijkstra(S, E, adj_dict):
    visited = [float("Inf")] * (N + 1)

    queue = [(0, S)]
    visited[S] = 0

    while queue:
        curr_cost, curr_node = heapq.heappop(queue)

        if curr_node == E:
            return curr_cost

        for next_node, next_cost in adj_dict[curr_node].items():
            next_cost += curr_cost
            if visited[next_node] > next_cost:
                visited[next_node] = next_cost
                heapq.heappush(queue, (next_cost, next_node))


if __name__ == "__main__":
    N, M, X = map(int, input().split())

    adj_dict = {v: {} for v in range(1, N + 1)}

    for _ in range(M):
        S, E, T = map(int, input().split())
        adj_dict[S][E] = T
    
    max_cost = 0

    for node in range(1, N + 1):
        if node != X:
            cost = dijkstra(node, X, adj_dict) + dijkstra(X, node, adj_dict)
            max_cost = max(max_cost, cost)
    
    print(max_cost)