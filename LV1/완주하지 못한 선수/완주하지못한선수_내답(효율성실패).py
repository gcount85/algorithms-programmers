participant = ["mislav", "stanko", "mislav", "ana"]	
completion = ["stanko", "ana", "mislav"]	


def solution(participant, completion):
    for i in completion:
        if i in completion:
            participant.remove(i)
    return participant[0]

solution(participant, completion)

