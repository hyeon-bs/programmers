def solution(my_string):
    answer = ''
    for i in my_string:
        if i.isupper():
            I = i.lower()
            answer = answer + I
        elif i.islower():
            U = i.upper()
            answer = answer + U
    return answer