def solution(a,b,incoluded):
    result = 0
    for i in range(len(incoluded)):
        if incoluded[i]:
            result = result+ (a + (b * i))

    return result

a = 3
b = 4
incoluded = [True,False,False,True,True]
print(solution(a,b,incoluded))