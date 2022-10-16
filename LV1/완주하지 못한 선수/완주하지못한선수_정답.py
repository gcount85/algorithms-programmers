
def solution(participant, completion):
    participant.sort()   
    completion.sort()
    for i in range(len(completion)):
        if completion[i] != participant[i]:
            answer = participant[i]
            break        # break를 사용해서 효율성이 올라간다 -> 리스트를 전체 다 돌 필요가 없어지니까!!!! 
        else:
            answer = participant[-1]
            
    
    return answer


