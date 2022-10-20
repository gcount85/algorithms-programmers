def solution(denum1, num1, denum2, num2):
    분자 = denum1*num2 + denum2*num1
    분모 = num1*num2
    # 분자 분모의 최대공약수로 나눠주자~ 
    for i in range(min(분자,분모),0,-1):
        if 분자%i ==0 and 분모%i==0:
            최대공약수 = i
            break
    return [분자/최대공약수, 분모/최대공약수]