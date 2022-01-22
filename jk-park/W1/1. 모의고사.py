# [완전탐색 lv1] 모의고사 -https://programmers.co.kr/learn/courses/30/lessons/42840?language=javascript ( 프로그래머스 )

def solution(answers):
    cnt_arr = [0, 0, 0]  # 정답 개수 저장하는 list, 0: a, 1: b, 2: c
    answer = []
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        if answers[i] == a[i % 5]:  # 모듈로 연산을 통해 모든 배열을 반복해서 돌아볼 수 있도록.
            cnt_arr[0] += 1
        if answers[i] == b[i % 8]:
            cnt_arr[1] += 1
        if answers[i] == c[i % 10]:
            cnt_arr[2] += 1

    answer = list(filter(lambda x: cnt_arr[x] == max(cnt_arr), range(len(cnt_arr))))
    answer = [x + 1 for x in answer]

    return answer

