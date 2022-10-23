#          0       1       2
lines = [[0, 5], [1, 0], [3, 0]]

def solution(lines):
    차이 = 0
    sort_line = sorted([sorted(i) for i in lines])
    a = sort_line[0][0]
    b = sort_line[1][0]
    c = sort_line[2][0]
    x = sort_line[0][1]
    y = sort_line[1][1]
    z = sort_line[2][1]
    xyz = sorted([x, y, z])
    print(xyz)
    if a == b == c:
        차이 = xyz[1] - a
    elif a < b == c:
        차이 = xyz[1] - b
    elif a == b < c:
        차이 = xyz[0] - a
        if xyz[1] > c:
            차이 += xyz[1] > c
        if xyz[0] > c:
            차이 -= (xyz[0] - c)
    elif a < b < c:
        if xyz[0] > b:
            차이 += xyz[0] - b
        if xyz[1] > c:
            차이 += xyz[1] - c
        if xyz[0] > c:
            차이 -= (xyz[0] - c)
    return 차이

print(solution(lines))