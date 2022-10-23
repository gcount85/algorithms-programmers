#          0       1       2
lines = [[0, 5], [3, 9], [1, 10]]

def solution(lines):
    차이 = 0
    [i.sort() for i in lines]
    lines.sort(key=lambda x: (x[0], x[1]))
    a = lines[0][0]
    b = lines[1][0]
    c = lines[2][0]
    x = lines[0][1]
    y = lines[1][1]
    z = lines[2][1]
    xyz = [x, y, z]
    xyz.sort()
    print(xyz)
    if a == b == c:
        차이 = xyz[1] - a
    elif a < b == c:
        차이 = y - b
    elif a == b < c:
        차이 = x - a
        if y > c:
            차이 += y - c
        if x > c:
            차이 -= (x - c)
    elif a < b < c:
        if x > b: 
            차이 += x - b
        if z < y:
            차이 += z - c
        if z > y:
            차이 += y - c
        if x > c:
            차이 -= (x - c)
    return 차이

print(solution(lines))