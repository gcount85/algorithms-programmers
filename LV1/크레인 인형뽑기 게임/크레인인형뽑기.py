board = [[0,0,0,0,0],
         [0,0,1,0,3],
         [0,2,5,0,1],
         [4,2,4,4,2],
         [3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
# result = 4
# 같은 숫자는 같은 인형을 의미
# moves의 원소는 board의 컬럼을 가리킴 => board[i]의 인덱스 번호+1
# 같은 숫자 두개(같은 인형 두개)가 바구니에 연속해서 쌓이게 되면 바구니에서 사라짐 
# 인형이 사라진 갯수를 result

def f(board, moves):
    bucket = []
    result = 0
    for i in moves:
        col_index = i-1
        for j in board:
            if j[col_index] != 0:
                bucket.append(j[col_index])
                j[col_index] = 0
                if (len(bucket) != 0) and (len(bucket) != 1): # 이 부분 그냥 len(bucket)>1이라고 하면 됨 
                    while bucket[-1] == bucket[-2]:
                        del bucket[-1]
                        del bucket[-1]
                        result += 2
                        if (len(bucket) == 0 or 1):
                            break
                break
    return result

# moves의 원소에 대하여 반복문
    # board의 원소에 대해 반복문    
        # moves[i]에 해당하는 board[i]의 인덱스 번호+1을 탐색 
        # if :0이 아닌 것을 만나면 그 숫자를 복사하여 bucket에 옮김 + 0으로 바꿈 
            # if bucket이 None 상태면 
                # continue, 지나가 
            # else : bucket[-2]가 bucket[-1]과 같으면
                # 둘이 삭제하고 result에 1추가   


f(board, moves)
