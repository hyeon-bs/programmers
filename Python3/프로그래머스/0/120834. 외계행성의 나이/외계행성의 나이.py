def solution(age):
    answer = ''
    info = {'a':'0','b':'1','c':'2','d':'3','e':'4','f':'5','g':'6','h':'7','i':'8','j':'9'}
    age = str(age)
    for i in age:
        for a, b in info.items():
            if i == b:
                answer = answer + a
    return answer