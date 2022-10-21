#          0      1        2        3
dots = [[1, 4], [9, 2], [3, 8], [10, 4]]

def solution(dots):
    lst = []
    
    for i in range(0,3):
        for j in range(1,4):
            if j > i:
                grad = (dots[j][1]-dots[i][1])/(dots[j][0]-dots[i][0])
                lst.append(grad)
    lst2 = set(lst)
    if len(lst2) != len(lst):
        return 1
    if len(lst2) == len(lst):
        return 0

print(solution(dots))