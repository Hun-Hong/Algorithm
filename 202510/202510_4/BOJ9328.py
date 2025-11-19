from collections import deque


if __name__ == "__main__":
    T = int(input())

    for _ in range(T):
        from pprint import pprint
        
        h, w = map(int, input().split())

        building = [list(input()) for _ in range(h)]

        keys = set(input())

        s_idx = []

        for i in range(h):
            if building[i][0] != "*":
                s_idx.append((i, 0))
            if building[i][w-1] != "*":
                s_idx.append((i, w-1))

        for j in range(w):
            if building[0][j] != "*":
                s_idx.append((0, j))
            if building[h-1][j] != "*":
                s_idx.append((h-1, j))
        
        visited = [[False] * w for _ in range(w)]

        queue = deque(s_idx)
        lock_dict = {}
        move_type = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]
        count = 0

        while queue:
            cur_i, cur_j = queue.popleft()
            
            if building[cur_i][cur_j].isupper():
                if building[cur_i][cur_j].lower() not in keys:
                    if lock_dict.get(building[cur_i][cur_j]):
                        lock_dict[building[cur_i][cur_j]].append((cur_i, cur_j))
                    else:
                        lock_dict[building[cur_i][cur_j]] = [(cur_i, cur_j)]

                    continue
            
            if building[cur_i][cur_j].islower():
                keys.add(building[cur_i][cur_j])
                if lock_dict.get(building[cur_i][cur_j].upper()):
                    for (i, j) in lock_dict.get(building[cur_i][cur_j].upper()):
                        queue.append((i, j))
            
            if building[cur_i][cur_j] == "$":
                count += 1
                building[cur_i][cur_j] = "."

            for m_i, m_j in move_type:
                next_i, next_j = cur_i + m_i, cur_j + m_j
                
                if 0 <= next_i < h and 0 <= next_j < w:
                    if building[next_i][next_j] != "*" and not visited[next_i][next_j]:
                        queue.append((next_i, next_j))
                        visited[next_i][next_j] = True
        
        print(count)