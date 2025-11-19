from collections import deque
from copy import deepcopy


def bfs(N, M, area):
    copy_area = deepcopy(area)

    queue = deque([])
    
    empty_space = 0
    for i in range(N):
        for j in range(M):
            if copy_area[i][j] == 0:
                empty_space += 1

            elif copy_area[i][j] == 2:
                queue.append((i, j))
    
    move_type = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    ]

    while queue:
        cur_i, cur_j = queue.popleft()

        for m_i, m_j in move_type:
            n_i, n_j = cur_i + m_i, cur_j + m_j
            if 0 <= n_i < N and 0 <= n_j < M:
                if copy_area[n_i][n_j] == 0:
                    copy_area[n_i][n_j] = 2
                    queue.append((n_i, n_j))
                    empty_space -= 1
    
    return empty_space


if __name__ == "__main__":
    N, M = map(int, input().split())

    area = [list(map(int, input().split())) for _ in range(N)]

    empty = []
    for i in range(N):
        for j in range(M):
            if area[i][j] == 0:
                empty.append((i, j))
    
    E = len(empty)
    max_area = 0
    for i in range(E):
        area[empty[i][0]][empty[i][1]] = 1
        for j in range(i+1, E):
            area[empty[j][0]][empty[j][1]] = 1
            for k in range(j+1, E):
                area[empty[k][0]][empty[k][1]] = 1
                empty_area = bfs(N, M, area)
                max_area = max(max_area, empty_area)
                area[empty[k][0]][empty[k][1]] = 0
            
            area[empty[j][0]][empty[j][1]] = 0
        
        area[empty[i][0]][empty[i][1]] = 0

    print(max_area)

