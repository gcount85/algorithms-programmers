#          0      1        2        3
dots = 	[[3, 5], [3, 1], [2, 4], [5, 10]]

def solution(dots):
    lst = []
    for i in range(0,3):
        for j in range(1,4):
            # 제로디비전 처리를 안 해주면 런타임 에러 뜸 
            if j > i and (dots[j][0]-dots[i][0]) != 0:  
                grad = (dots[j][1]-dots[i][1])/(dots[j][0]-dots[i][0])
                if grad in lst:
                    return 1
                lst.append(grad)
    return 0

print(solution(dots))