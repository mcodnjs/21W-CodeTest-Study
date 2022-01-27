def publish(progress, speed):
    days = (100 - progress) / speed
    # 만약 days가 딱 떨어지면 days 이후 배포날이되고,
    # 소수점이 발생하면 days+1일 이후가 배포날이 됨.
    
    if type(days)==type(1):
        return days
    else:
        return int(days) + 1

def solution(progresses, speeds):
    answer = []
    
    idx = 0 # 기능을 가리키는 포인터
    while(idx < len(progresses)): # 기능 수 대로 돌면 멈춤
        count = 0 # 한 배포에 몇 기능을 배포했는지
        days = publish(progresses[idx], speeds[idx])
        idx += 1
        count += 1
        if( idx >= len(progresses)):
            answer.append(count)
            break
        before = 1 # 앞에서 하나라도 100을 못넘었으면 0으로 바꿈
        for i in range(idx, len(progresses)):
            progresses[i] = progresses[i] + days * speeds[i]
            if(progresses[i] >= 100 and before):
                idx += 1
                count += 1
            else:
                before = 0
        answer.append(count)
    
    return answer