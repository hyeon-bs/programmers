def solution(my_string):
    answer = ''
    vowel = 'aeiou'
    for i in my_string:
        for j in vowel:
            if i == j:
                my_string = my_string.replace(i,'')
            elif i == ' ':
                my_string = my_string.replace(i,' ')
    answer = my_string
    return answer