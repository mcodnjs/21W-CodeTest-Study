def solution(answers):
    answer = []
    
    grades = [0,0,0]
    student_A = [1,2,3,4,5]
    student_B = [2,1,2,3,2,4,2,5]
    student_C = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(0, len(answers)):
        if(student_A[(i+len(student_A)) % len(student_A)] == answers[i]):
            grades[0] += 1
        if(student_B[(i+len(student_B)) % len(student_B)] == answers[i]):
            grades[1] += 1
        if(student_C[(i+len(student_C)) % len(student_C)] == answers[i]):
            grades[2] += 1
        
    idx = 0
    for grade in grades:
        if(grade == max(grades)):
            answer.append(idx+1)
        idx += 1
    
