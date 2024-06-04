import math

def solution(n):
    answer = 0
    result = 0
    if n-6 == 0:
        answer = 1
    elif n-6 > 0:
        answer = ((n*6) // math.gcd(n,6)) // 6
    else:
        answer = ((n*6) // math.gcd(n,6)) // 6
    return answer