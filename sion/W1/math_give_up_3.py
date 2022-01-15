def solution(answers):
    answer = []
    
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]
    
    count = [0] * 3
    for i in range(len(answers)):
        i1 = i % len(s1)
        i2 = i % len(s2)
        i3 = i % len(s3)
        if s1[i1] == answers[i]:
            count[0] += 1
        if s2[i2] == answers[i]:
            count[1] += 1
        if s3[i3] == answers[i]:
            count[2] += 1
            
    max_count = max(count)
    for i in range(len(count)):
        if count[i] == max_count:
            answer.append(i+1)
    
    return answer
