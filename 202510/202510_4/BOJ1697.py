if __name__ == "__main__":
    from collections import deque
    N, K = map(int, input().split())

    visited = [-1] * 100001

    visited [N] = 0
    queue = deque([])
    queue.append(N)

    while queue:
        curr_num = queue.popleft()
        if curr_num == K:
            result = visited[curr_num]
            break

        for mv in range(3):
            if mv == 0:
                next_num = curr_num + 1
            elif mv == 1:
                next_num = curr_num - 1
            elif mv == 2:
                next_num = curr_num * 2
            
            if 0 <= next_num <= 100000:
                if visited[next_num] == -1:
                    visited[next_num] = visited[curr_num] + 1
                    queue.append(next_num)
    
    print(result)