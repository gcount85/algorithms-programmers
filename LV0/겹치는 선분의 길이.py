#          0       1       2
lines = [[0, 5], [3, 9], [1, 10]]	
def solution(lines):
    차이 = 0
    lines.sort()
    # [[0, 5], [1, 10], [3, 9]]
    for i in range(2):
        if lines[i][1] < lines[i+1][1]:
            if (lines[i][1]-lines[i+1][0]) > 0:
                차이 += lines[i][1]-lines[i+1][0]
        if lines[i][1] > lines[i+1][1]:
            차이 += lines[i+1][1]-lines[i+1][0]
        if i == 0 and lines[i][1] > lines[i+2][0]:
            차이 -= lines[i][1]-lines[i+2][0]

    return 차이

print(solution(lines))