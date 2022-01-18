def grading(m, n, board):
    copy_board = [[0] * n for i in range(m)]
    
    # TODO 네모 위치에 1씩 더함, 나중에 0이 아닌 값의 수를 리턴해야함
    for i in range(n-1):
        for j in range(m-1):
            if( (board[i][j] == board[i][j+1]) and (board[i][j] == board[i+1][j])):
                if(board[i+1][j] == board[i+1][j+1]):
                    copy_board[i][j] += 1
                    copy_board[i][j+1] += 1
                    copy_board[i+1][j] += 1
                    copy_board[i+1][j+1] += 1

def solution(m, n, board):
    answer = 0
    return answer
