def solution(my_string, letter):
    answer = ''
    for i in my_string:
        if i != letter:
            answer = answer + i
        else:
            continue
    return answer