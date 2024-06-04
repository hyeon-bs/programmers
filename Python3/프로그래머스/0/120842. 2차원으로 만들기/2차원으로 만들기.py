def solution(num_list, n):
    answer = [[]]
    result = []
    lenght = []
    for i in range(0,len(num_list),n):
        for j in range(n):
            result.append(num_list[i+j])
        lenght.append(result)
        result = []
    answer = [k for k in lenght]
    return answer
    