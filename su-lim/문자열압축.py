def compression(s, unit):
    number = len(s)//unit
    if(len(s)%unit > 0):
        number += 1

    repeat = 1
    str_unit = []
    result_str = ""
    
    for i in range(number): # unit 단위로 잘라서 단어 블록들을 리스트에 넣음
        start = i*unit
        fin = (i*unit)+unit
        str_unit.append(s[start:fin])
    
    for i in range(len(str_unit)):
        if(i != len(str_unit)-1): # 마지막이 아니면
            if(str_unit[i] == str_unit[i+1]):
                repeat += 1
            else:
                if(repeat == 1):
                    result_str += str_unit[i]
                else:
                    result_str += (str(repeat) + str_unit[i])
                    repeat = 1
        else: # 마지막 일때
            if(repeat == 1):
                result_str += str_unit[i]
            else:
                result_str += (str(repeat) + str_unit[i])
                repeat = 1

    return len(result_str)
            
def solution(s):
    
    s_len = len(s)
    answer = s_len
    
    # 1부터 max(문자열 길이의 1/2)까지로 잘라야 최소한의 압축 효과가 있음, max를 넘어가서 자르면 압축효과X
    max = int(len(s)/2)
    
    for unit in range(1,max+1): #1 ~ max 값까지 잘라가면서 가장 압축이 잘되는 값을 찾음
        c_len = compression(s, unit)
        if(c_len < s_len): # 새로운 단위(Unit)로 자른 값이 더 작게 압축되면 answer를 바꿈
            s_len = c_len
            answer = c_len
    
    return answer
