n = 1000
import sys

def solution(n):
    # 최대 재귀 깊이를 1000보다 높게 설정 
    sys.setrecursionlimit(10000)
    if n == 1:
        return 0
    elif n % 2 != 0:
        return solution(n-1)
    elif n % 2 == 0:
        return n + solution(n-1) 

print(solution(n))
