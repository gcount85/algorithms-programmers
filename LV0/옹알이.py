babbling = ["ayayeayayeayaye" ]	
발음 = ["aya", "ye", "woo", "ma"]

def solution(babbling):
    c = 0
    for i in babbling:
        for j in 발음:
            if i == j:
                c += 1
            elif i.startswith(j) and i != j:
                last = j
                c += a(i, j, last, c)

    return c


def a(i, j, last, c):
    for k in 발음:
        if k != last:
            if i == (j+k):
                c += 1
                return c
            elif i.startswith(j+k) and i != (j+k):
                last = k
                a(i, j+k, last, c)

print(solution(babbling))
