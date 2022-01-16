# [문자열 lv2 ] 문자열 압축 - https://programmers.co.kr/learn/courses/30/lessons/60057 (2020 카카오 블라인드 채용)

def solution(s):

    answer = 0

    for i in range(len(s)//2+2):
        temp_str = ''
        temp_res = ''
        chk_cnt = 1
        if i == 0:
            continue
        temp_str = s[:i]
        for j in range(i, len(s)+i, i): # i부터 시작해서 i의 단위로 비교하기
            cmp_str = s[j:i+j] # 현재 j의 위치에서 istep만큼을 cmp에 넣는다
            if temp_str == cmp_str:
                chk_cnt+=1 #
            else: # 같은 문자열 검사가 종료된 후 후처리
                if chk_cnt == 1: # 같은 문자가 없다면
                    temp_res += temp_str
                else:
                    temp_res = temp_res + str(chk_cnt) + temp_str
                temp_str = s[j:j+i]
                chk_cnt = 1
                print(temp_res)
        if answer == 0:
            answer = len(temp_res)
        else:
            answer = min(answer, len(temp_res))
    return answer

s = 'aabbaccc'
print(solution(s))
