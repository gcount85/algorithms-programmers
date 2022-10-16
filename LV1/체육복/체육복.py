def solution(n, lost, reserve):
    받은애들 = 0
    lost_copy = lost[:]
    for i in lost:
        if i in reserve:
            lost_copy.remove(i)
            reserve.remove(i)
    if lost_copy is not None:
        for i in lost_copy:
            if (i+1) in reserve and (i-1) in reserve:
                받은애들 += 1
                reserve.remove(i+1)
            elif ((i+1) in reserve) or ((i-1) in reserve):
                if (i+1) in reserve:
                    받은애들 += 1
                    reserve.remove(i+1)
                elif (i-1) in reserve:
                    받은애들 += 1
                    reserve.remove(i-1)
        answer = n - len(lost_copy) + 받은애들
    if lost_copy is None:
        answer = n 