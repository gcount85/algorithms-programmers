lines = [[1, 5], [1, 0], [3, 99]]

import collections
def solution(lines):
    # 각 선분마다 1만큼의 범위 나타내기
    # lines의 각각의 원소 리스트의 x, y에 대해서 range로 최소값과 최댓값까지 숫자 리스트를 만들고,
    # 최소값부터 최대값까지 (숫자, 숫자+1)의 튜플 생성(각 선분마다 1만큼의 범위를 일일이 표시해주는 것)
    # 정답에서는 generator 형식으로 만들어주었으나, 나는 프린트하기 위해 일반 리스트 []를 이용함 
    min_to_max = [(i, i + 1) for x, y in lines for i in range(min(x, y), max(x, y))]

    # 범위 개수 세기
    # 각 선분의 1의 범위를 포함하는 튜플의 개수를 counter를 이용하여 갯수를 셈
    # Counter는 dict 형식으로 반환하므로 item() 속성을 이용하여 k, v로 표시함 
    # dict_items((k, v) ...) 이렇게 k, v가 튜플 형식으로 보임 
    overlapped_line = collections.Counter(min_to_max).items()

    # 2개 이상 겹쳐진 범위의 선분 세기
    # 겹치는 선분들에 대해서 두 개 이상의 선분이 지나가야 하므로, 
    # 겹치는 선분의 숫자를 나타내는 v가 2, 3인 범위만 1로 치환하여 합한다
    length = sum(1 for k, v in overlapped_line if v > 1)

    return length

print(solution(lines))
