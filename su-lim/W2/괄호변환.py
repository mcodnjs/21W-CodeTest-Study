# myReverse : ( -> ), ) -> ( 문자 치환
def myReverse(s):
    dic = {'(':')', ')':'('}
    tmp = ""
    
    for i in s:
        tmp += dic[i]
    return tmp

# right() : 올바른 괄호 문자열 인지 판단
def right(s):
    stack = []

    for i in s:
        if i == '(':
            stack.append('(')
        else:
            try:
                stack.pop()
            except:
                return False

    if stack: # 안 비어있으면
        return False
    else:
        return True

def recursion(w):
    if not w: # empty string
        return w
    
    u = ""
    v = ""
    idx = 0
    
    # Step 2
    for idx in range(0, len(w), 2):
        u += w[idx:idx+2]
        if u.count("(") == u.count(")"):
            break
    v = w[idx+2:]
    
    # Step 3
    if right(u):
        u += recursion(v)
        return u
    
    # Step 4
    else:
        s = "("
        s += recursion(v)
        s += ")"
        s += myReverse(u[1:len(u)-1])
        return s

def solution(p):
    answer = recursion(p)
    return answer