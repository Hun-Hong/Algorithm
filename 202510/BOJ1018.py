if __name__ == "__main__":
    N, M = map(int, input().split())

    board = [list(input()) for _ in range(N)]
    from pprint import pprint
    
    min_paint = 32

    def color_check(board):
        global min_paint

        base_color = ["W", "B"]
        paint = 0
        for i in range(8):
            for j in range(8):
                if board[i][j] != base_color[(i+j) % 2]:
                    paint += 1
        
        if paint > 32:
            paint = 64 - paint

        min_paint = min(min_paint, paint)
                        


    for i in range(N-7):
        for j in range(M-7):
            cut_board = [row[j:j+8] for row in board[i:i+8]]
            color_check(cut_board)
    
    print(min_paint)