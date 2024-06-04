def solution(sides):
    answer = 0
    sides.sort()
    if sides[2] == sides[1] + sides[0]:
        answer = 2
    elif sides[2] > sides[1] + sides[0]:
        answer = 2
    elif sides[2] < sides[1] + sides[0]:
        answer = 1
    return answer