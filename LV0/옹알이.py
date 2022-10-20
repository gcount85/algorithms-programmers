babbling = ["aya", "yee", "u", "maa"]
발음들 = ["aya", "ye", "woo", "ma"]

def solution(babbling):
    c = 0
    for 옹알 in babbling:
        for 발음 in 발음들:
            if 발음 == 옹알:
                c += 1
                break
            elif 옹알.startswith(발음+발음):
                break
            elif 옹알.startswith(발음) and 옹알 != 발음:
                last = 발음
                c = a(옹알, 발음, last, c)
                break
    return c

def a(옹알, 발음, last, c):
    for 다음발음 in 발음들:
        if 다음발음 != last:
            if 옹알 == (발음+다음발음):
                c += 1
                return c
            elif 옹알.startswith(발음+다음발음) and 옹알 != (발음+다음발음):
                last = 다음발음
                return a(옹알, 발음+다음발음, last, c)   # 재귀함수 부분에 return을 해주어야 함! 
    return c   # yee 같은 케이스를 위해서 필요함 return 0은 안됨 

print(solution(babbling))
