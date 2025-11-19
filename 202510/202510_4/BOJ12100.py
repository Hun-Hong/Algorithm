def run_2048(board, direction):
    new_board = []
    if direction == 0:
        for i in range(N):
            row = [num for num in board[i] if num != 0]
            j = 0
            new_row = []
            while j < len(row):
                if j+1 < len(row):
                    if row[j] == row[j+1]:
                        new_row.append(row[j] * 2)
                        j += 2
                    else:
                        new_row.append(row[j])
                        j += 1
                else:
                    new_row.append(row[j])
                    j += 1
                    
            row = new_row + (N - len(new_row)) * [0]
            new_board.append(row)
            
    if direction == 1:
        for i in range(N):
            row = [num for num in board[i][::-1] if num != 0]
            j = 0
            new_row = []
            while j < len(row):
                if j+1 < len(row):
                    if row[j] == row[j+1]:
                        new_row.append(row[j] * 2)
                        j += 2
                    else:
                        new_row.append(row[j])
                        j += 1
                else:
                    new_row.append(row[j])
                    j += 1
                    
            row = (N - len(new_row)) * [0] + new_row[::-1]
            new_board.append(row)

    if direction == 2:
        board = list(zip(*board))
        for i in range(N):
            row = [num for num in board[i] if num != 0]
            j = 0
            new_row = []
            while j < len(row):
                if j+1 < len(row):
                    if row[j] == row[j+1]:
                        new_row.append(row[j] * 2)
                        j += 2
                    else:
                        new_row.append(row[j])
                        j += 1
                else:
                    new_row.append(row[j])
                    j += 1
                    
            row = (N - len(new_row)) * [0] + new_row[::-1]
            new_board.append(row[::-1])
        new_board = list(map(list, zip(*new_board)))

    if direction == 3:
        board = list(zip(*board))
        for i in range(N):
            row = [num for num in board[i][::-1] if num != 0]
            j = 0
            new_row = []
            while j < len(row):
                if j+1 < len(row):
                    if row[j] == row[j+1]:
                        new_row.append(row[j] * 2)
                        j += 2
                    else:
                        new_row.append(row[j])
                        j += 1
                else:
                    new_row.append(row[j])
                    j += 1
                    
            row = new_row + (N - len(new_row)) * [0] 
            new_board.append(row[::-1])
        new_board = list(map(list, zip(*new_board)))
    
    return new_board


if __name__ == "__main__":
    # from pprint import pprint
    import sys

    input = sys.stdin.readline
    N = int(input())

    board = [list(map(int, input().split())) for _ in range(N)]

    max_value = 0

    new_board = run_2048(board, 1)

    stack = []
    stack.append((board, 0))

    while stack:
        curr_board, curr_time = stack.pop()
        
        if curr_time == 5:
            value = max(max(row) for row in curr_board)
            max_value = max(max_value, value)
            continue

        for direction in range(4):
            new_board = run_2048(curr_board, direction)
            stack.append((new_board, curr_time + 1))
    
    print(max_value)
            
'''
5
0 0 2 0 0
0 0 0 0 0
2 0 0 0 0
0 0 0 0 0
0 0 0 0 0
'''