def solution(n):
    a = 0
    while True:
        a +=1
        if a*6%n == 0:
            return a
        
n = 10
print(solution(n))