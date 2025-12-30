def solution(order):
    a = []
    sm = []
    while True:
        if '3' in order:
            a.append(1)
        if '6' in order:
            a.append(1)
        if '9' in order:
            a.append(1)
        
        
        sm = sum(a)
        return sm

order = '93645'
print(solution(order))