def solution(dot):
    answer = 0
    x = dot[0]
    y = dot[1]
    
    if 0 < x and 0 < y:
        answer = 1
    elif 0 > x and 0 < y:
        answer = 2
    elif 0 > x and 0 > y:
        answer = 3
    elif 0 < x and 0 > y:
        answer = 4
    else: 
        answer = 0
    return answer