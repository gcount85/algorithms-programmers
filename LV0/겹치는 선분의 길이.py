#          0       1       2
lines = [[0, 5], [3, 9], [1, 3]]	
def solution(lines):
    차이 = 0
    lines.sort(key=lambda x: (x[0], x[1]))
    print(lines)
    for i in range(2):
        if lines[i][1] <= lines[i+1][0]:
            continue
        if lines[i][1] > lines[i+1][0]:
            if lines[i][1] > lines[i+1][1]:
                차이 += lines[i+1][1]-lines[i+1][0]
            else:
                차이 += lines[i][1]-lines[i+1][0]
    if lines[0][1] > lines[2][0]:
        if lines[0][1] > lines[2][1]:
            차이 += lines[2][1]-lines[2][0]
        else:
            차이 += lines[0][1]-lines[2][0]
    if lines[0][1] > lines[2][0] and lines[1][1] > lines[2][0]:
        차이 -= lines[0][1]-lines[2][0]
    return 차이

print(solution(lines))