def solution(array, height):
    answer = 0
    result = []
    
    for i in range(len(array)):
        if height < array[i]:
            answer+= 1
        else:
            answer = 0
    return answer