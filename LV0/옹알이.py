babbling = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]	
발음 = ["aya", "ye", "woo", "ma"]

def solution(babbling):
    c = 0
    for i in babbling:
        for j in 발음:
            if i == j:
                c += 1
            elif i.startswith(j) and i != j:
                for k in 발음:
                    if k != j and i == (j+k):
                        c += 1
                    elif i.startswith(j+k) and i != (j+k):
                        for l in 발음:
                            if l != k and i == (j+k+l):
                                c += 1  
                            elif i.startswith(j+k+l) and i != (j+k+l):
                                for m in 발음:
                                    if m != l and i == (j+k+l+m):
                                        c += 1
    
    return c

print(solution(babbling))
