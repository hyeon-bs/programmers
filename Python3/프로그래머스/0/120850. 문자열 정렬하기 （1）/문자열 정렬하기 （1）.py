def solution(my_string):
    answer = []
    result = ''
    num = '0123456789'
    
    for i in my_string:
        for j in num:
            if i == j:
                result = result + i
    answer = list(map(int, result))
    answer.sort()
    return answer