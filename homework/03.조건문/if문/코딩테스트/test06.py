def solution(n):
    while True:
        if n > 0:
            n / 2
            n = n + 1
        elif n < 0:
             n - 1
             n / 2
             n = n + 1
        if n == 1:
            break
    return n

num_list = [12,4,15,1,14]
print(solution(num_list))