def solution(n,control):
    math = {'w':1, 's':-1, 'd':10, 'a':-10}
    for b in control:
        n += math[b]

    return n