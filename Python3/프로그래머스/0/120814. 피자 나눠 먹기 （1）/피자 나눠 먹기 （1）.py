def solution(n):
    answer = 0
    for i in range(n):
        if n-7 <= 0:
            answer +=1
            break
        else:
            answer += 1
            n = n-7
            continue
    return answer