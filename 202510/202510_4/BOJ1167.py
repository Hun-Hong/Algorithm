from collections import deque
import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    V = int(input())
    
    adj_dict = {v: {} for v in range(1, V + 1)}

    for _ in range(V):
        V_num, *edges = map(int, input().split())
        for i in range(len(edges)//2):
            node, cost = edges[i*2], edges[i*2+1]
            adj_dict[V_num][node] = cost

    diameter = 0
    visited = [-1] * (V + 1)
    queue = deque([])
    
    queue.append(1)
    visited[1] = 0
    while queue:
        curr_node = queue.popleft()

        for next_node, next_cost in adj_dict[curr_node].items():
            if visited[next_node] == -1:
                visited[next_node] = next_cost + visited[curr_node]
                queue.append(next_node)
    far_idx = visited.index(max(visited))
    
    visited = [-1] * (V + 1)
    queue = deque([])
    
    queue.append(far_idx)
    visited[far_idx] = 0
    while queue:
        curr_node = queue.popleft()

        for next_node, next_cost in adj_dict[curr_node].items():
            if visited[next_node] == -1:
                visited[next_node] = next_cost + visited[curr_node]
                queue.append(next_node)
    
    print(max(visited))