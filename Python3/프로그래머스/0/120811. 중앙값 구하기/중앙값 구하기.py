def solution(array):
    answer = 0
    result = len(array)//2
    array.sort()
    answer = array[result]
    
    return answer