def solution(survey, choices):
    score = {4: 0, 3:1, 5:1, 2:2, 6:2, 1:3, 7:3}
    type_score = {}

    for i, v in enumerate(survey):
        for character in v:
            if character not in list(type_score.keys()):
                type_score.setdefault(character, 0)
        if choices[i] == 4:
            continue
        if choices[i] < 4:
            type_score[v[0]] = type_score[v[0]] + score[choices[i]]
        if choices[i] > 4:
            type_score[v[1]] = type_score[v[0]] + score[choices[i]]
    
    type_order = {}

    
    RT = [{k:v} for k, v in type_score.items() if k in ['R', 'T']]
    CF = [{k:v} for k, v in type_score.items() if k in ['C', 'F']]
    JM = [{k:v} for k, v in type_score.items() if k in ['J', 'M']]
    AN = [{k:v} for k, v in type_score.items() if k in ['A', 'N']]
    
    type_order.update(zip([0, 1, 2, 3], [RT, CF, JM, AN]))
    
    default_type = ['R', 'C', 'J', 'A']
    for v in type_order.values():
        v.sort(reverse=True, key=lambda x:(list(x.values()), list(x.keys())))
    answer_lst = [list(v[0].keys()) if v != [] else [default_type[k]] for k, v in type_order.items()]

    answer = "".join(sum(answer_lst, []))
    print(answer)

    
    return answer

# survey = ["AN", "CF", "MJ", "RT", "NA"]
# choices = [5, 3, 2, 7, 5]
survey = ["TR", "RT", "TR"]
choices = [7, 1, 3]

solution(survey, choices)
# survey	choices	result

# 비동의<->동의                        비동의<->동의  
# ["TR", "RT", "TR"]	[7, 1, 3]	"RCJA"

# 선택지의 절대값에 따라 점수가 같음 
# 모든 질문의 성격 유형 점수를 다 더해 각 지표에서 가장 높은 점수를 받은 유형이 검사결과 
# 점수가 같으면 오름차순 정렬하여 표시 