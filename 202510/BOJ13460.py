from copy import deepcopy


def gravitate(board, direction):
    new_board = deepcopy(board)
    balls = {"B", "R"}
    ball_idx = [None, None]
    R_finished = False

    if direction == 0:
        for j in range(M):
            for i in range(N):
                curr_i, curr_j = i, j
                if new_board[curr_i][curr_j] in balls:
                    ball = new_board[curr_i][curr_j]
                    while True:
                        if new_board[curr_i-1][curr_j] == "O":
                            if ball == "B":
                                return False, None
                            elif ball == "R":
                                R_finished = True
                                new_board[curr_i][curr_j] = "."
                                break
                        if new_board[curr_i-1][curr_j] == ".":
                            new_board[curr_i-1][curr_j], new_board[curr_i][curr_j] = new_board[curr_i][curr_j], new_board[curr_i-1][curr_j]
                            curr_i -= 1
                        else:
                            if ball == "B":
                                ball_idx[0] = curr_i, curr_j
                            else:
                                ball_idx[1] = curr_i, curr_j
                            break

    elif direction == 1:
        for j in range(M):
            for i in range(N-1,-1,-1):
                curr_i, curr_j = i, j
                if new_board[curr_i][curr_j] in balls:
                    ball = new_board[curr_i][curr_j]
                    while True:
                        if new_board[curr_i+1][curr_j] == "O":
                            if ball == "B":
                                return False, None
                            elif ball == "R":
                                R_finished = True
                                new_board[curr_i][curr_j] = "."
                                break
                        if new_board[curr_i+1][curr_j] == ".":
                            new_board[curr_i+1][curr_j], new_board[curr_i][curr_j] = new_board[curr_i][curr_j], new_board[curr_i+1][curr_j]
                            curr_i += 1
                        else:
                            if ball == "B":
                                ball_idx[0] = curr_i, curr_j
                            else:
                                ball_idx[1] = curr_i, curr_j
                            break

    elif direction == 2:
        for i in range(N):
            for j in range(M):
                curr_i, curr_j = i, j
                if new_board[curr_i][curr_j] in balls:
                    ball = new_board[curr_i][curr_j]
                    while True:
                        if new_board[curr_i][curr_j-1] == "O":
                            if ball == "B":
                                return False, None
                            elif ball == "R":
                                R_finished = True
                                new_board[curr_i][curr_j] = "."
                                break
                        if new_board[curr_i][curr_j-1] == ".":
                            new_board[curr_i][curr_j-1], new_board[curr_i][curr_j] = new_board[curr_i][curr_j], new_board[curr_i][curr_j-1]
                            curr_j -= 1
                        else:
                            if ball == "B":
                                ball_idx[0] = curr_i, curr_j
                            else:
                                ball_idx[1] = curr_i, curr_j
                            break

    elif direction == 3:
        for i in range(N):
            for j in range(M-1,-1,-1):
                curr_i, curr_j = i, j
                if new_board[curr_i][curr_j] in balls:
                    ball = new_board[curr_i][curr_j]
                    while True:
                        if new_board[curr_i][curr_j+1] == "O":
                            if ball == "B":
                                return False, None
                            elif ball == "R":
                                R_finished = True
                                new_board[curr_i][curr_j] = "."
                                break
                        if new_board[curr_i][curr_j+1] == ".":
                            new_board[curr_i][curr_j+1], new_board[curr_i][curr_j] = new_board[curr_i][curr_j], new_board[curr_i][curr_j+1]
                            curr_j += 1
                        else:
                            if ball == "B":
                                ball_idx[0] = curr_i, curr_j
                            else:
                                ball_idx[1] = curr_i, curr_j
                            break
    
    if R_finished:
        return True, None
    else:
        return new_board, ball_idx


if __name__ == "__main__":
    from pprint import pprint
    from collections import deque

    N, M = map(int, input().split())

    board = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if board[i][j] == "B":
                B_idx = (i, j)
                board[i][j] = "."
            if board[i][j] == "R":
                R_idx = (i, j)
                board[i][j] = "."
            if board[i][j] == "O":
                O_idx = (i, j)

    visited = {}
    visited[(*B_idx, *R_idx)] = 0

    queue = deque([(*B_idx, *R_idx)])
    result = False

    while queue:
        B_i, B_j, R_i, R_j = queue.popleft()
        curr_time = visited[(B_i, B_j, R_i, R_j)]
        if curr_time > 10:
            break

        for direction in range(4):
            curr_board = deepcopy(board)
            curr_board[B_i][B_j] = "B"
            curr_board[R_i][R_j] = "R"

            new_board, ball_idx = gravitate(curr_board, direction)

            if new_board == True:
                result = curr_time + 1
                break
            elif new_board != False:
                # pprint(new_board)
                # print(ball_idx)
                new_idx = (*ball_idx[0], *ball_idx[1])
                if visited.get(new_idx, float("Inf")) > curr_time + 1:
                    visited[new_idx] = curr_time + 1
                    queue.append(new_idx)
                
        if result:
            break
    
    if result and (result <= 10):
        print(result)
    else:
        print(-1)