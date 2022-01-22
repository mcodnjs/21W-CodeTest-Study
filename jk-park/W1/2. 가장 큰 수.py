# [정렬 lv2] 가장 큰 수 -https://programmers.co.kr/learn/courses/30/lessons/42746?language=javascript ( 프로그래머스 )

def solution(numbers):
    answer = ''
    single_digit_cnt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 0~9 한자리수의 개수 파악
    string_list = []
    one_list = []
    zero_cnt = 0
    temp_str = ''
    for i in range(len(numbers)):
        if numbers[i] == 1000:
            one_list.append('1000')
            continue
        if numbers[i] == 100:
            one_list.append('100')
            continue
        if numbers[i] == 10:
            one_list.append('10')
            continue

        if numbers[i] > 99:
            numbers[i] = float(numbers[i]) / float(100)  # 소수 만들기
            temp_str = str(numbers[i])
            if len(temp_str) == 3:  # 110, 120 ...
                temp_str + '0'
            string_list.append(temp_str)
        elif numbers[i] > 9:
            numbers[i] = float(numbers[i]) / float(10)
            temp_str = str(numbers[i])

            string_list.append(temp_str)
        else:
            if numbers[i] == 0:
                zero_cnt += 1
                continue
            temp_str = f'{numbers[i]}.{numbers[i]}{numbers[i]}'
            single_digit_cnt[numbers[i]] += 1  # 추후에 한자리수로 되돌리기 위해 cnt를 올려준다.
            string_list.append(temp_str)
    string_list.sort(reverse=True)
    one_list.sort()
    string_list.extend(one_list)
    for i in range(zero_cnt):
        string_list.append('0')


    for i in range(len(single_digit_cnt)):
        if i == 0:
            continue
        if single_digit_cnt[i] > 0:
            for j in range(single_digit_cnt[i]):
                single_temp = string_list.index(f'{i}.{i}{i}')
                string_list[single_temp] = f'{i}'

    character = '.'
    string_list = ''.join(string_list)
    answer = ''.join(x for x in string_list if x not in character)  # . 빼기

    return answer


# numbers = [0, 1000, 3, 5, 10, 120, 100]
numbers =  [3, 30, 34, 5, 9]
# # numbers = [3, 30, 34, 5, 9]
# numbers = [1, 10, 100, 1000, 0]
print(solution(numbers))
