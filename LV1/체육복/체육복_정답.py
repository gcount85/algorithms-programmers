

def solution(n, lost, reserve):
    set_reserve = set(reserve)-set(lost)
    set_lost = set(lost)-set(reserve)

    for i in set_reserve:       # 빌려주는 애 입장에서 먼저 생각하기 
        if (i-1) in set_lost:
            set_lost.remove(i-1)
        elif (i+1) in set_lost:
            set_lost.remove(i+1)
    answer = n - len(lost) 

    print(answer)
    return answer


n=10
lost=[1, 3, 5, 7]
reserve=[2, 3, 4, 5, 6, 8]
solution(n, lost, reserve)