def solution(my_string):
    answer = 0
    result = []
    for i in range(len(my_string)):
        i = str(i)
        for j in my_string:
            if i == j:
                result.append(i)
    result = map(int,result)
    answer = sum(result)
    return answer