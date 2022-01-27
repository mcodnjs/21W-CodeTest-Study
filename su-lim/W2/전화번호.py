def solution(phone_book):
    answer = True
    phone_book.sort()
    
    for current, idx in zip(phone_book, range(len(phone_book)-1)):
        if current == phone_book[idx+1][:len(current)]:
            return False

    return answer