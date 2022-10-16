def solution(babbling):
    발음 = ["aya", "ye", "woo", "ma"]
    가능한발음 = [i+j for i in 발음 for j in 발음 if i != j]
    print(가능한발음)
    c = 0
    # for i in 발음:
    #     if i in babbling:            
    #         c += 1
    # for i in 가능한발음:
    #     if i in babbling:
    #         c += 1
            
    for i in babbling:
        for j in 발음:
            if i == j:
                c += 1
            elif i.startswith(j) and i != j:
                for k in 발음:
                    if k != j:
                        if i == (j+k):
                            c += 1
    
    
    return c