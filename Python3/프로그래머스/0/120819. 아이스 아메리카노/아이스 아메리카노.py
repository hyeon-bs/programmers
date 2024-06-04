def solution(money):
    answer = []
    count = 0
    
    if money - 5500 < 0:
        answer = [0,0]
    else:
        while money - 5500 >= 0:
            money = money - 5500
            count+= 1
            
    answer = [count, money]
    return answer