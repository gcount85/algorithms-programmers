survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]

def solution(survey, choices):

    my_dict = {"RT":0,"CF":0,"JM":0,"AN":0}
    
    for A, B in zip(survey,choices):
        B -= 4
        if A not in my_dict:
            A = A[::-1]
            B *= -1
        my_dict[A] += B

    print(my_dict)

    result = ""

    for k, v in my_dict.items():
        if v == 0:
            result += k[0]
        if v > 0:
            result += k[1]
        if v < 0:
            result += k[0]


    return result

