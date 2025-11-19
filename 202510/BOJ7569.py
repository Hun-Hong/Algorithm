from collections import deque
if __name__ == "__main__":

    M, N, H = map(int, input().split())
    box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
    tomato = 0

    queue = deque([])

    for k in range(H):
        for i in range(N):
            for j in range(M):
                if box[k][i][j] == 1:
                    queue.append((i, j, k))
                elif box[k][i][j] == 0:
                    tomato += 1
    if tomato > 0:
        move_type = [
        (-1, 0, 0),
        (1, 0, 0),
        (0, -1, 0),
        (0, 1, 0),
        (0, 0, -1),
        (0, 0, 1),
        ]
        max_value = 0
        while queue:
            cur_i, cur_j, cur_k = queue.popleft()
            # print(cur_i, cur_j, cur_k)
            for m_i, m_j, m_k in move_type:
                n_i, n_j, n_k = cur_i + m_i, cur_j + m_j, cur_k + m_k
                if 0 <= n_i < N and 0 <= n_j < M and 0 <= n_k < H:
                    if box[n_k][n_i][n_j] == 0:
                        box[n_k][n_i][n_j] = box[cur_k][cur_i][cur_j] + 1
                        max_value = max(box[cur_k][cur_i][cur_j] + 1, max_value)
                        queue.append((n_i, n_j, n_k))
                        tomato -= 1

        if tomato > 0:
            print(-1)
        else:
            print(max_value - 1)

    else:
        print(0)

    