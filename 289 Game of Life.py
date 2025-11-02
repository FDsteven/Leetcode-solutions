def gameOfLife(board):
    """
    :type board: List[List[int]]
    :rtype: None Do not return anything, modify board in-place instead.
    """
    m = len(board)
    n = len(board[0])
    num_of_lives = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            up = down = left = right = upleft = upright = downleft = downright = 0
            current_point = board[i][j]
            if i > 0:
                up = board[i-1][j]
                if j> 0:
                    upleft = board[i-1][j-1]
                if j < (n-1):
                    upright = board[i-1][j+1]
            if i < (m - 1):
                down = board[i+1][j]
                if j < (n-1):
                    downright = board[i+1][j+1]
                if j > 0:
                    downleft = board[i+1][j-1]
            if j > 0:
                left = board[i][j-1]
            if j < (n-1):
                right = board[i][j+1]
            num_of_lives[i][j] = up+down+left+right+upleft+upright+downleft+downright
    for i in range(m):
        for j in range(n):
            if board[i][j] == 1:
                if (num_of_lives[i][j] < 2) or (num_of_lives[i][j] > 3):
                    board[i][j] = 0
            else:
                if num_of_lives[i][j] == 3:
                    board[i][j] = 1
                
    return board
board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
print(gameOfLife(board))