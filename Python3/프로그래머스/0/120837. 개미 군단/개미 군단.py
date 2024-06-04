def solution(hp):
    answer = 0
    count = 0
    for i in range(hp):
        if hp >= 5:
            hp = hp - 5
            count+= 1
        elif 3 <= hp < 5:
            hp = hp - 3
            count+= 1
        elif 1 <= hp < 3:
            hp = hp - 1
            count+= 1
        elif hp == 0:
            break
    answer = count
        
    return answer