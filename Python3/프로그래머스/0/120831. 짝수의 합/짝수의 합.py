def solution(n):
    answer = 0
    result = []
    for i in range(1, n+1):
        if 2 * i <= n:
            result.append(2*i)
    answer = sum(result)
        
    return answer