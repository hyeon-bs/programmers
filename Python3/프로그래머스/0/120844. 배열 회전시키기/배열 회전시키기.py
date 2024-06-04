def solution(numbers, direction):
    answer = []
    num = numbers[0]
    if direction == 'right':
        numbers.insert(0,numbers[-1])
        numbers.pop()
    elif direction == 'left':
        numbers.append(num)
        del numbers[0]
    answer = numbers
    return answer