board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]
import numpy as np

def solution(board):
    b_arr = np.array(board)
    tmp = np.where(b_arr == 1)  # 앞은 row, 뒤는 column
    index = zip(tmp[0], tmp[1])
    for i in index:
        tmp_arr = b_arr[i[0]-1:i[0]+2, i[1]-1:i[1]+2]
        tmp_arr += 1
    array2 = (b_arr == 0).astype(int)
    return int(sum(sum(array2)))

print(solution(board))