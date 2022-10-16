import re

# new_id = "...!@BaT#*..y.abcdefghijklm"

def solution(new_id):
    id = new_id
    id = id.lower()
    id = re.sub('[^a-z0-9-_.]', '', id)
    id = re.sub('[.]{2,}', '.', id)
    id = re.sub('\A[.]|[.]\Z', '', id)      # 여기!
    if id == "":
        id = "a"
    if len(id) >= 16:
        id = id[:15]
    id = re.sub('[.]\Z', '', id)
    while len(id) <= 2:
        id += id[-1]

    # print(id)



        
    return id



new_id = "...!@BaT#*..y.abcdefghijklm"
# new_id = "z-+.^."
# new_id = "**s......."


solution(new_id)

