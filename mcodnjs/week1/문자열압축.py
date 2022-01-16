def func(string_list):
    num = 0
    remain = []
    temp = 0 # 10 넘는지 확인하는 용도               #제 코드랑 달라서 그런지 이 부분 아주 흥미있게 잘 봤습니다. 신박하네요~ Good~
    for idx, data in enumerate(string_list):
        if idx == len(string_list)-1:
            remain.append(data)
            break
        if data == string_list[idx+1]:
            if temp == 0 or temp == 8: 
                num += 1
            temp += 1
        else: 
            temp = 0
            remain.append(data)
    return num + len(''.join(remain))
    
def solution(s):
    answer = 0
    length = []
    for i in range(1,len(s)+1): # 자르는 단위      #최대 반복은 s의 절반 그러니까 문자열 길이가 8이라면 4가 2번 반복되는게 최대이기 때문에 시간효율을 고려해서 len(s)//2로 설정하는 것도 Not Bad
        j = 0
        string_list = []
        while j < len(s): # 문자열 길이  
            string_list.append(s[j: j+i])       # 자를 때 while문으로 해도 상관은 없지만 for문에 인자 3개 집어 넣어서 범위를 지정해서 자르는것도 좋은 방법일것 같습니다 ㅎㅎ
            j = j + i                           # for j in range(0, len(s), i+1)을 while문 대신에 쓸수 있습니닷
        length.append(func(string_list))
        
    answer = min(length)
    return answer
