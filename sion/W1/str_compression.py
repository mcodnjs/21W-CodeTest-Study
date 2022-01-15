def solution(s):
    result = []
    
		# 1일 때 따로 처리
    one_result = ''
    one_tmp = s[0]
    one_count = 1
    for i in range(1, len(s)):
        if s[i] == one_tmp[-1]:
            one_count += 1
            one_tmp = str(one_count) + s[i]
        else:
            one_result += one_tmp
            one_tmp = s[i]
            one_count = 1
    
    one_result += one_tmp
    
    # print(one_result)
    result.append(len(one_result))
            

    # 2부터 처리하는 코드
    max_l = len(s)//2
    for i in range(1, max_l+1):
        tmp_result = ''
        tmp = ''
        count = 1
        for j in range(0, len(s), i):
            # print(s[j:j+i], i, '개씩 자름', s)
            if j == 0:
                tmp = s[j:j+i]
                continue
            if s[j:j+i] == tmp[-i:]:
                count += 1
                tmp = str(count) + s[j:j+i]
            else:
                tmp_result += tmp
                tmp = s[j:j+i]
                count = 1
            # print('tmp:', tmp, '중간결과:', tmp_result)
        tmp_result += tmp
        # print('-------------리얼결과: ', tmp_result)
        
        result.append(len(tmp_result))
        # print(tmp_result, len(tmp_result))
    # print(result)
        
    
    return min(result)
