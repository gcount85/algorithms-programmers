
numbers = "onetwothreefourfivesixseveneightninezero"
def solution(numbers):
    eng = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    answer = numbers
    for i, v in enumerate(eng):
        answer = answer.replace(v,f"{i}") # str(num)을 이용해도 됨 

    return int(answer)

print(solution(numbers))