import math
numbers	= [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
# numbers	= [9] * 3
hand = "left"
# LRLLLR L LRRL
# LRLLLR R LLRRL
    # if 숫자가 1,4,7 = L
    # if 숫자가 3,6,9 = R

def solution(numbers, hand):
    class Point2D:
        def __init__(self, x, y):
            self.x = x
            self.y = y
    answer = ''
    position = {'R':'#', 'L':'*'}
    for num in numbers:
        if num in [1, 4, 7]:
            position['L'] = num
            answer += 'L'
        elif num in [3, 6, 9]:
            position['R'] = num
            answer += 'R'
        else:
            x = [-1, 0, 1] * 4
            y = [3, 3, 3, 2, 2, 2, 1, 1, 1, 0, 0, 0]
            좌표 = {A:B for A, B in zip([1, 2, 3, 4, 5, 6, 7, 8, 9, '*', 0, '#'], list(zip((x), (y))))}
            print(좌표)
            왼손좌표 = Point2D(x=좌표[position['L']][0], y=좌표[position['L']][1])    
            오른손좌표 = Point2D(x=좌표[position['R']][0], y=좌표[position['R']][1]) 
            n의좌표 = Point2D(x=좌표[num][0], y=좌표[num][1])
            
            # 왼손좌표와의 거리 구하기   
            a = n의좌표.x - 왼손좌표.x    # 선 a의 길이
            b = n의좌표.y - 왼손좌표.y    # 선 b의 길이
            왼손거리 = math.sqrt((a * a) + (b * b))    # (a * a) + (b * b)의 제곱근을 구함
            # print(왼손거리)
            
            # 오른손좌표의 거리 구하기
            a = n의좌표.x - 오른손좌표.x    # 선 a의 길이
            b = n의좌표.y - 오른손좌표.y    # 선 b의 길이
            오른손거리 = math.sqrt((a * a) + (b * b))    # (a * a) + (b * b)의 제곱근을 구함

            if 왼손거리 > 오른손거리:
                position['R'] = num
                answer += 'R'
            elif 왼손거리 < 오른손거리:
                position['L'] = num
                answer += 'L'
            else: 
                if hand == 'right':
                    position['R'] = num
                    answer += 'R'
                elif hand == 'left':
                    position['L'] = num
                    answer += 'L'



    # if 숫자 in 2,5,8,0
        # 왼오의 포지션 확인
            # 포지션 다름
                # 포지션 차이가 적은 애 반환
                    # 1위 : 2,5,8일때 값의 차이가 1이거나 3 // 0일때 8,*,#
                    # 2위 : 2,5,8일때 값의 차이가 2, 4, //8일때 *, # // 0일때 7,9
                    # 3위 : 값의 차이가 6 // 5일때 0 // 0일때 5
                    # 4위 : 2,8일때 값의 차이가 5나 7 // 5일때 *, # // 0일때 4,6
                    # 5위 : 2일때 0,       
            # 포지션 같음
                # hand에 따라 반환 

    print(answer)
    return answer




solution(numbers, hand)