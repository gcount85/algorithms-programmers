from collections import Counter

def solution(id_list, report, k):
    id_dict = {i:set() for i in id_list}
    for i in report:
        user_id = i.split(" ")[0]
        reported_id = i.split(" ")[1]
        id_dict[user_id].add(reported_id)

    total_reported_id = sum(list(map(list, id_dict.values())), [])
    c = Counter(total_reported_id)
    mailing_list = [name for name, v in c.items() if v >= k]

    mailing_dict = {i:0 for i in id_list}
    for k, v in id_dict.items():
        for id in mailing_list:
            if id in v:
                mailing_dict[k] += 1
    
    answer = list(mailing_dict.values())

    return answer

# 5. id_dict[i]의 밸류 set에 메일링리슽트에 존재하는 원소가 있으면 {idlist:0}의 밸류에 +1
#각 유저별로 처리 결과 메일을 받은 횟수=그사람이 신고해서 정지먹인 아이디 개수 
# 1. id_dict = {i:{} for i in id_list}
# 반복문: report의 i에 대해 ->  
# 조건: idlist[i] == report[i][0] -> id_dict의 value set에 어펜드 
# 2. id_dict 밸류의 set의 value를 모두 sum하여 1차원 리스트로 바꿈
# 3. 그 일차원 리스트를 카운트 
# 4. k개 이상 존재하는 원소를 메일링리스트에 어펜드 [프로도, 무지, 네오]

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2 

solution(id_list, report, k)