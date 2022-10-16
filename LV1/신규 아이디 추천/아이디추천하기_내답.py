# new_id = "...!@BaT#*..y.abcdefghijklm"

def solution(new_id):

    answer = ""

    for i, v in enumerate(new_id):
        if v.isupper():
            v = v.lower()
        elif not (v.isalpha() or v.isdigit()) and (v not in ["-", "_", "."]):
            v = ""
        answer += v

    while ".." in answer:
        answer = answer.replace("..", ".")

    if answer == "":
        answer = "a"
    if answer[0] == ".":
        answer = answer[1:]
        if answer == "":
            answer = "a"
    if answer[-1] == ".":
        answer = answer[:-1]
        if answer == "":
            answer = "a"
    print(answer)
    if len(answer) >= 16:
        answer = answer[:15]    
        if answer[-1] == ".":
            answer = answer[:-1]
    while len(answer) <= 2:
        answer += answer[-1]



        
    return answer



# new_id = "...!@BaT#*..y.abcdefghijklm"
# new_id = "z-+.^."
new_id = "**s......."


print(solution(new_id))

