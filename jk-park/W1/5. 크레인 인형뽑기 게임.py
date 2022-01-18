# [시뮬레이션  lv1 ] 크레인 인형뽑기 게임 - https://programmers.co.kr/learn/courses/30/lessons/64061 (2019 카카오 개발자 겨울 인턴십)

# [시뮬레이션  lv1 ] 크레인 인형뽑기 게임 - https://programmers.co.kr/learn/courses/30/lessons/64061 (2019 카카오 개발자 겨울 인턴십)

def solution(board, moves):
    answer = 0
    basket = []
    n = len(board)
    for i in range(len(moves)):
        for j in range(n):
            if board[j][moves[i]-1] != 0:
                basket.append(board[j][moves[i]-1])
                board[j][moves[i]-1] = 0
                break

        if len(basket)>=2 and basket[len(basket)-1] == basket[len(basket)-2]:
            basket.pop()
            basket.pop()
            answer += 2
    return answer

board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = []
print(solution(board, moves))