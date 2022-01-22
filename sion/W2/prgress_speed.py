import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    days = []
    n = len(progresses)
    for i in range(n):
        days.append(math.ceil((100-progresses[i])/speeds[i]))
        
    while days:
        first_day = days[0]
        count = 0
        for i in range(len(days)):
            days[i] -= first_day
            if days[i] <= 0:
                count += 1
            else: break
        answer.append(count)
        
        days = deque(days)
        for _ in range(count):
            days.popleft()
    
    return answer
